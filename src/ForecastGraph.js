import React from 'react';
import { Line } from 'react-chartjs-2';

const ForecastGraph = ({ labels, forecastValues }) => {
    const data = {
        labels: labels,
        datasets: [
            {
                label: 'Demand Forecast',
                data: forecastValues,
                fill: false,
                borderColor: 'rgb(75, 192, 192)',
                tension: 0.1,
            },
        ],
    };

    return (
        <div>
            <h2>Demand Forecast Graph</h2>
            <div style={{ height: '400px', width: '600px' }}>
                <Line data={data} />
            </div>
        </div>
    );
};

export default ForecastGraph;
