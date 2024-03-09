const openai = require('openai');

const openaiClient = new openai.OpenAI(process.env.OPENAI_API_KEY);

async function generateText(prompt) {
    try {
        const response = await openaiClient.complete({
            engine: 'text-davinci-002',
            prompt: prompt,
            maxTokens: 50,
            stop: ['\n'],
        });

        const generatedText = response.data.choices[0].text.trim();

        return generatedText;
    } catch (error) {
        console.error('Error generating text:', error);
        throw error;
    }
}

module.exports = {
    generateText
};
