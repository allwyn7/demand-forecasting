const { OpenLLM } = require('openllm');

// Initialize the OpenLLM model
const openllmModel = new OpenLLM();

// Function to generate text using OpenLLM
async function generateText(prompt) {
    try {
        // Generate text based on the prompt using OpenLLM
        const generatedText = await openllmModel.generateText(prompt);

        return generatedText;
    } catch (error) {
        console.error('Error generating text:', error);
        throw error;
    }
}

module.exports = {
    generateText
};
