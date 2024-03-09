import React, { useState } from 'react';
import Button from '../components/Button';
import TextInput from '../components/TextInput';

function MyComponent() {
    const [interpretation, setInterpretation] = useState('');
    const [loading, setLoading] = useState(false);

    const handleTextInputSubmit = async (text) => {
        try {
            setLoading(true);
            const response = await fetch('http://localhost:5000/interpret', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ prompt: text })
            });

            if (!response.ok) {
                throw new Error('Failed to interpret user input');
            }

            const data = await response.json();
            setInterpretation(data.interpretation);
        } catch (error) {
            console.error('Error interpreting user input:', error);
        } finally {
            setLoading(false);
        }
    };

    const handleButtonClick = () => {
        console.log('Button clicked');
    };

    return (
        <div className="my-component-container">
            <TextInput onSubmit={handleTextInputSubmit} />
            <Button onClick={handleButtonClick} label="Click Me" />
            {loading && <p>Loading...</p>}
            {interpretation && (
                <div className="interpretation-container">
                    <h3>Interpretation:</h3>
                    <p>{interpretation}</p>
                </div>
            )}
        </div>
    );
}

export default MyComponent;
