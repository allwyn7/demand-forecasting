import React, { useState } from 'react';
import './TextInput.css';

const TextInput = ({ onSubmit }) => {
    const [inputText, setInputText] = useState('');

    const handleChange = (e) => {
        setInputText(e.target.value);
    };

    const handleSubmit = () => {
        onSubmit(inputText);
        setInputText('');
    };

    return (
        <div className="text-input-container">
            <input type="text" value={inputText} onChange={handleChange} className="text-input-field" />
            <button onClick={handleSubmit} className="submit-button">Submit</button>
        </div>
    );
};

export default TextInput;
