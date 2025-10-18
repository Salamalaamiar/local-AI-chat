import React ,{useState} from 'react';
import './chatbox.css'

const ChatBox =()=>{

    const [messages , setMessages]=useState([]);
    const [input , setInput]=useState('');
    const [loading , setLoading]=useState(false);

    const handleSend=async()=>{

        if (!input.trim()) return;
        setLoading(true);


        const userMessage={role:'user' , content:input};
        setMessages(prev =>[...prev, userMessage]);

        try {
            const response= await fetch('http://127.0.0.1:8000/chat', {
                method: 'Post',
                headers:{'Content-Type':'application/json'},
                body: JSON.stringify({message:input}),
            });


            const data=await response.json();
            setMessages(prev=> [...prev ,{role:'assistant', content: data.reply}]);
            } catch(error){
                setMessages(prev => [...prev, { role: 'assistant', content: 'Error connecting to AI.' }]);
            }

            setInput('');
            setLoading(false);

        
    };
    return(
        <div className="chat-container">
            <div className="messages">
                {messages.map((msg,i)=>(
                    <div key={i} className={msg.role}>
                        <strong> {msg.role==='user'? 'You:':'AI:'} </strong>{msg.content}
                    </div>    
                ))}

            </div>

            <div className='input-area'>
                <input
                type="text"
                value={input}
                onChange={e=>setInput(e.target.value)}
                placeholder='Ask me something ...'

                />

                <button onClick={handleSend} disabled={loading}> 
                    {loading?'thinking...':'Send'}
                </button>
            </div>
        </div>
    );


};

export default ChatBox;