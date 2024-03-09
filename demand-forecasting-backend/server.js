const express = require('express');
const openai = require('openai');
const gptService = require('./services/gptService');
const mlModelService = require('./services/mlModelService');

const app = express();

app.use(express.json());

const openaiClient = new openai.OpenAI(process.env.OPENAI_API_KEY);

app.post('/interpret', async (req, res) => {
    try {
        //llm starts
        const { prompt } = req.body;

        const interpretation = await gptService.generateText(openaiClient, prompt);
        //llm ends

        const predictions = await mlModelService.predict(interpretation);

        res.json({ predictions });
    } catch (error) {
        console.error('Error interpreting user input:', error);
        res.status(500).json({ error: 'An internal server error occurred' });
    }
});

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
