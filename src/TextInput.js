import React, { useState } from 'react';

const TextInput = ({ onSubmit }) => {
    const [inputText, setInputText] = useState('');

    const handleChange = (e) => {
        setInputText(e.target.value);
    };

    const handleSubmit = () => {
        onSubmit(inputText);
        setInputText(''); // Clear input after submission
    };

    return (
        <div>
            <input type="text" value={inputText} onChange={handleChange} />
            <button onClick={handleSubmit}>Submit</button>
        </div>
    );
};

export default TextInput;
