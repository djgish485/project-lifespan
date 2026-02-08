import argparse
import sys
import subprocess
from pathlib import Path
import datetime

def load_theory(theory_path):
    """Loads the content of a theory file."""
    try:
        with open(theory_path, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: Theory file not found at {theory_path}")
        sys.exit(1)

def call_claude(system_prompt, user_prompt):
    """Calls the Claude CLI with the given prompts."""
    try:
        # We use -p for print mode (non-interactive)
        cmd = [
            "claude", 
            "-p", user_prompt, 
            "--system-prompt", system_prompt
        ]
        
        # Run the command and capture output
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return result.stdout.strip()
        
    except subprocess.CalledProcessError as e:
        print(f"Error calling Claude CLI: {e}")
        print(f"Stderr: {e.stderr}")
        return f"[Error generating response: {e.stderr}]"
    except FileNotFoundError:
        print("Error: 'claude' CLI not found. Please ensure it is installed and in your PATH.")
        sys.exit(1)

def construct_system_prompt(role, theory_name, theory_content=None, rival_theory_name=None):
    if role == "proponent":
        return f"""You are the leading proponent of {theory_name}. 
Your goal is to posit it as the best explanation for aging. 
You are participating in a formal Popperian debate.
Adhere to the following content but expand using your general knowledge:
{theory_content}

Defend your theory against criticisms from {rival_theory_name}.
Be concise, rigorous, and focus on empirical evidence.
"""
    elif role == "critic":
        return f"""You are a ruthless Popperian critic representing {theory_name}. 
Your goal is to find logical inconsistencies, lack of falsifiability, and empirical data that contradicts {rival_theory_name}'s claims.
Reference your own theory's strengths where applicable:
{theory_content}
"""
    elif role == "judge":
        return """You are a neutral epistemologist. 
You do not pick a 'winner' based on rhetoric, but on which explanation remains less falsified and more explanatory. 
You identify the *Crucial Experiment* that would settle the dispute.
"""
    else:
        return ""

def main():
    parser = argparse.ArgumentParser(description="Conduct a Popperian debate using local Claude CLI.")
    parser.add_argument("--blue", required=True, help="Path to the Blue Team (Proponent) theory markdown file.")
    parser.add_argument("--red", required=True, help="Path to the Red Team (Critic) theory markdown file.")
    parser.add_argument("--rounds", type=int, default=2, help="Number of debate rounds.")
    parser.add_argument("--output", help="Output file path for the transcript.")
    
    args = parser.parse_args()

    blue_path = Path(args.blue)
    red_path = Path(args.red)
    
    blue_name = blue_path.stem.replace("_", " ").title()
    red_name = red_path.stem.replace("_", " ").title()

    print(f"Starting Debate: {blue_name} (Blue) vs. {red_name} (Red)")
    print("Using local 'claude' CLI for all agents.")

    blue_content = load_theory(blue_path)
    red_content = load_theory(red_path)

    # The transcript acts as the shared context
    transcript = f"# Debate: {blue_name} vs. {red_name}\n\nDate: {datetime.date.today()}\n\n"

    # --- Round 1: Opening Statement (Blue) ---
    print("\n--- Round 1: Opening Statement (Blue) ---")
    sys_prompt = construct_system_prompt("proponent", blue_name, blue_content, red_name)
    user_prompt = "Make your opening statement. Present your strongest evidence and your riskiest prediction. Keep it under 400 words."
    
    response = call_claude(sys_prompt, user_prompt)
    
    transcript += f"## Round 1: Opening Statement ({blue_name})\n\n{response}\n\n"
    print("Blue Team finished.")

    # --- Loop for Rounds ---
    for i in range(1, args.rounds + 1):
        # Red Turn (Refutation/Critique)
        print(f"\n--- Round {i+1}: Refutation ({red_name}) ---")
        sys_prompt = construct_system_prompt("critic", red_name, red_content, blue_name)
        # Context is the last turn from Blue
        context = f"Here is the debate so far:\n\n{transcript}\n\n"
        user_prompt = f"{context}Refute the arguments made by {blue_name}. Point out contradictions or empirical failures. Keep it under 400 words."
        
        response = call_claude(sys_prompt, user_prompt)
        transcript += f"## Round {i+1}: Critique ({red_name})\n\n{response}\n\n"
        print("Red Team finished.")

        # Blue Turn (Defense)
        print(f"\n--- Round {i+1}: Defense ({blue_name}) ---")
        sys_prompt = construct_system_prompt("proponent", blue_name, blue_content, red_name)
        context = f"Here is the debate so far:\n\n{transcript}\n\n"
        user_prompt = f"{context}Defend against the criticisms from {red_name}. Clarify your position or provide counter-evidence. Keep it under 400 words."
        
        response = call_claude(sys_prompt, user_prompt)
        transcript += f"## Round {i+1}: Defense ({blue_name})\n\n{response}\n\n"
        print("Blue Team finished.")

    # --- Verdict (Judge) ---
    print("\n--- Final Verdict (Judge) ---")
    sys_prompt = construct_system_prompt("judge", "Judge")
    context = f"Here is the full debate transcript:\n\n{transcript}\n\n"
    user_prompt = f"{context}Summarize the debate. Identify the fundamental disagreement. Propose a *Crucial Experiment* (concrete, feasible) that would distinguish between the two theories."
    
    response = call_claude(sys_prompt, user_prompt)
    transcript += f"## Judge's Verdict\n\n{response}\n\n"
    print("Judge finished.")

    # Save
    if args.output:
        with open(args.output, 'w') as f:
            f.write(transcript)
        print(f"\nTranscript saved to {args.output}")
    else:
        print("\n" + transcript)

if __name__ == "__main__":
    main()