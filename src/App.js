import React, { useState } from 'react';
import TextInput from './TextInput';
import Button from './Button';
import ForecastGraph from './ForecastGraph';

const App = () => {
  const [interpretedText, setInterpretedText] = useState('');
  const [forecastData, setForecastData] = useState({});

  const handleTextSubmit = (text) => {
    // Simulate backend interpretation
    setInterpretedText(`Interpreted: ${text}`);
  };

  const handleForecastRequest = () => {
    // Simulate backend demand forecasting
    const labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'];
    const forecastValues = [100, 150, 200, 180, 220, 250];
    setForecastData({ labels, forecastValues });
  };

  return (
    <div>
      <h1>Demand Forecasting Application</h1>
      <TextInput onSubmit={handleTextSubmit} />
      <div>{interpretedText}</div>
      <Button onClick={handleForecastRequest} label="Get Forecast" />
      {forecastData.labels && <ForecastGraph labels={forecastData.labels} forecastValues={forecastData.forecastValues} />}
    </div>
  );
};

export default App;
