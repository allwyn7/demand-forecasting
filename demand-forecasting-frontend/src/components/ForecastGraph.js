import React from 'react';
import { Line } from 'react-chartjs-2';
import './ForecastGraph.css';

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
        <div className="forecast-graph-container">
            <h2 className="graph-title">Demand Forecast Graph</h2>
            <div className="graph-wrapper">
                <Line data={data} />
            </div>
        </div>
    );
};

export default ForecastGraph;
