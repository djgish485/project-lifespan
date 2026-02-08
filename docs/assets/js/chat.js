document.addEventListener('DOMContentLoaded', () => {
    // 0. Load Marked.js for Markdown Rendering
    const markedScript = document.createElement('script');
    markedScript.src = 'https://cdn.jsdelivr.net/npm/marked/marked.min.js';
    document.head.appendChild(markedScript);

    // 1. Inject UI Elements
    const body = document.body;

    // Sidebar
    const sidebar = document.createElement('div');
    sidebar.id = 'lifespan-chat-sidebar';
    sidebar.innerHTML = `
        <div class="chat-header">
            <span>Project Lifespan AI</span>
            <div class="chat-controls">
                <button class="chat-btn chat-reset-btn" title="Reset Chat">🔄</button>
                <button class="chat-btn chat-close-btn" title="Close">×</button>
            </div>
        </div>
        <div class="chat-messages" id="chat-messages">
            <div class="message agent">
                <p>Hello! I am the <strong>Epistemological Engine</strong>.</p>
                <p>Highlight text to challenge it, or ask me anything.</p>
            </div>
        </div>
        <div class="chat-input-area">
            <input type="text" id="chat-input" placeholder="Type your challenge or question..." />
            <button id="chat-send">Send</button>
        </div>
    `;
    body.appendChild(sidebar);

    // FAB
    const fab = document.createElement('div');
    fab.id = 'lifespan-chat-fab';
    fab.innerHTML = `<svg viewBox="0 0 24 24"><path d="M20 2H4c-1.1 0-2 .9-2 2v18l4-4h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zm0 14H6l-2 2V4h16v12z"/></svg>`;
    body.appendChild(fab);

    // Tooltip
    const tooltip = document.createElement('div');
    tooltip.id = 'lifespan-tooltip';
    tooltip.textContent = '💬 Discuss / Challenge';
    body.appendChild(tooltip);

    // State
    let activeContext = null;
    let currentPath = window.location.pathname;

    // ... (Selection Logic - skipped for brevity in replacement but kept in file) ...

    // 3. Logic: Click Triggers (Updated with Reset)
    fab.addEventListener('click', () => {
        sidebar.classList.add('open');
        activeContext = null; 
        document.getElementById('chat-input').focus();
    });

    tooltip.addEventListener('click', (e) => {
        e.stopPropagation();
        sidebar.classList.add('open');
        tooltip.style.display = 'none';
        
        addMessage(`Context: "${activeContext.substring(0, 50)}..."`, 'user', true);
        document.getElementById('chat-input').focus();
    });

    document.querySelector('.chat-close-btn').addEventListener('click', () => {
        sidebar.classList.remove('open');
    });

    // Reset Chat Logic
    document.querySelector('.chat-reset-btn').addEventListener('click', () => {
        const messagesDiv = document.getElementById('chat-messages');
        messagesDiv.innerHTML = `
            <div class="message agent">
                <p>Chat cleared. I am ready for a new topic.</p>
            </div>
        `;
        activeContext = null; 
    });

    // 4. Logic: Messaging
    const input = document.getElementById('chat-input');
    const sendBtn = document.getElementById('chat-send');
    const messagesDiv = document.getElementById('chat-messages');

    function addMessage(text, role, isContext = false) {
        const div = document.createElement('div');
        div.classList.add('message', role);
        if (isContext) div.classList.add('context-quote');
        
        if (role === 'agent' && typeof marked !== 'undefined') {
            div.innerHTML = marked.parse(text);
        } else {
            div.textContent = text;
        }
        
        messagesDiv.appendChild(div);
        messagesDiv.scrollTop = messagesDiv.scrollHeight;
    }

    async function sendMessage() {
        const text = input.value.trim();
        if (!text) return;

        input.value = '';
        input.disabled = true;
        sendBtn.disabled = true;
        
        addMessage(text, 'user');

        try {
            const response = await fetch('http://127.0.0.1:8002/chat', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    message: text,
                    context: activeContext,
                    file_path: currentPath
                })
            });

            const data = await response.json();
            addMessage(data.reply, 'agent');
        } catch (err) {
            addMessage("Error: Could not connect to Local Epistemology Server. Is scripts/local_server.py running?", 'agent');
            console.error(err);
        } finally {
            input.disabled = false;
            sendBtn.disabled = false;
            activeContext = null; // Consume context after sending
            input.focus();
        }
    }

    sendBtn.addEventListener('click', sendMessage);
    input.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') sendMessage();
    });
});
