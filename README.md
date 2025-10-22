# 🏃‍♂️ Fitness Data Analytics Dashboard
<div align="center">

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg?logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.30+-red.svg?logo=streamlit&logoColor=white)](https://streamlit.io)
[![Pandas](https://img.shields.io/badge/Pandas-2.1+-green.svg?logo=pandas&logoColor=white)](https://pandas.pydata.org)
[![Plotly](https://img.shields.io/badge/Plotly-5.20+-purple.svg?logo=plotly&logoColor=white)](https://plotly.com)
[![Windows](https://img.shields.io/badge/Windows-PowerShell-blue.svg?logo=windows&logoColor=white)](https://microsoft.com/windows)
[![License](https://img.shields.io/badge/License-Educational-orange.svg)](LICENSE)

</div>

<div align="center">

[![GitHub](https://img.shields.io/badge/GitHub-sunbyte16-black?style=for-the-badge&logo=github)](https://github.com/sunbyte16)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Sunil%20Kumar-blue?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/sunil-kumar-bb88bb31a/)
[![Portfolio](https://img.shields.io/badge/Portfolio-Visit%20Now-brightgreen?style=for-the-badge&logo=netlify)](https://lively-dodol-cc397c.netlify.app)

**Created By 💻 Sunil Sharma **

</div>

> 📊 A comprehensive web-based dashboard for analyzing and visualizing fitness data from Fitbit and Strava exports. Built with Streamlit, this application provides interactive data exploration capabilities for various fitness metrics including activity levels, heart rate, sleep patterns, and more.

## ✨ Features

- 📈 **Interactive Data Visualization**: Dynamic charts and graphs using Plotly
- 📊 **Multiple Dataset Support**: Handles daily, hourly, and minute-level fitness data
- ⚡ **Smart Data Loading**: Automatic sampling for large datasets to ensure optimal performance
- 🔍 **Real-time Analysis**: Live data profiling and statistical summaries
- 🎨 **Responsive Design**: Clean, professional interface optimized for data exploration

## 📋 Supported Data Types

- 🚶 **Daily Activity Metrics** (steps, calories, distance)
- 😴 **Sleep Analysis** (duration, efficiency, patterns)
- ❤️ **Heart Rate Monitoring** (second-level granularity)
- 💪 **Intensity Levels** (sedentary, light, moderate, vigorous)
- ⚖️ **Weight Tracking** and Body Composition
- 🔥 **Calorie Burn Analysis**

## 📋 Prerequisites

- 🐍 **Python**: 3.10 or higher
- 💻 **Operating System**: Windows (PowerShell support required)
- 📁 **Data**: Fitbit/Strava CSV export files

## 🚀 Installation & Setup

### 🎯 Option 1: Automated Setup (Recommended)

```powershell
# Clone or download the project
# Navigate to project directory
./run.ps1
```

The script automatically:

- ✅ Creates a Python virtual environment
- ✅ Installs all dependencies
- ✅ Launches the dashboard
- ✅ Opens your default browser

### ⚙️ Option 2: Manual Setup

```powershell
# Create virtual environment
py -m venv .venv

# Activate environment
.\.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Launch dashboard
streamlit run .\app\streamlit_app.py
```

## 📖 Usage

1. 🚀 **Start the Application**: Run the setup commands above
2. 🌐 **Access Dashboard**: Open your browser to `http://localhost:8501`
3. 📊 **Select Dataset**: Use the sidebar to choose from available data sources
4. 🔍 **Explore Data**: View summaries, create visualizations, and analyze trends
5. ⚙️ **Customize Views**: Adjust sampling rates and visualization parameters

## 📁 Project Structure

```
├── app/
│   └── streamlit_app.py      # Main dashboard application
├── Data Files/               # Fitness data exports (CSV format)
├── .venv/                    # Python virtual environment
├── requirements.txt          # Python dependencies
├── run.ps1                   # Automated setup script
└── README.md                 # Project documentation
```

## ⚙️ Configuration

### 📂 Data Directory

The application expects data files in the following structure:

```
Data Files/mturkfitbit_export_4.12.16-5.12.16/Fitabase Data 4.12.16-5.12.16/
```

To use different data sources, update the `DATA_DIR` path in `app/streamlit_app.py`.

### ⚡ Performance Optimization

- 📊 **Large Files**: Datasets over 50MB are automatically sampled
- 📈 **Row Limits**: Adjust "Max rows to load" in the sidebar (default: 250,000)
- 🧠 **Memory Management**: Application uses efficient data loading strategies

## 📦 Dependencies

| Package                                                                       | Version | Purpose                           |
| ----------------------------------------------------------------------------- | ------- | --------------------------------- |
| ![Streamlit](https://img.shields.io/badge/Streamlit-≥1.30-red?logo=streamlit) | ≥1.30   | Web application framework         |
| ![Pandas](https://img.shields.io/badge/Pandas-≥2.1-green?logo=pandas)         | ≥2.1    | Data manipulation and analysis    |
| ![Plotly](https://img.shields.io/badge/Plotly-≥5.20-purple?logo=plotly)       | ≥5.20   | Interactive visualization library |

## 🔧 Troubleshooting

### ⚠️ Common Issues

| Issue                           | Solution                                                                                                                                   |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| 📁 **Data Directory Not Found** | • Verify the data folder path matches the expected structure<br>• Update `DATA_DIR` in `streamlit_app.py` if using different data location |
| 🐌 **Performance Issues**       | • Reduce "Max rows to load" for large datasets<br>• Ensure sufficient system memory for data processing                                    |
| 🐍 **Python Environment**       | • Confirm Python 3.10+ is installed and accessible via `py` command<br>• Verify PowerShell execution policy allows script execution        |

## 🤝 Contributing

1. 🍴 Fork the repository
2. 🌿 Create a feature branch
3. ✏️ Make your changes
4. 🧪 Test thoroughly
5. 📤 Submit a pull request

[![Contributors Welcome](https://img.shields.io/badge/Contributors-Welcome-brightgreen.svg?style=flat)](CONTRIBUTING.md)

## 📄 License

This project is available for educational and research purposes. Please ensure compliance with data privacy regulations when using personal fitness data.

[![License: Educational](https://img.shields.io/badge/License-Educational-orange.svg)](LICENSE)

---

## 📞 Support

If you encounter any issues or have questions:

- 🐛 [Report a Bug](../../issues/new?template=bug_report.md)
- 💡 [Request a Feature](../../issues/new?template=feature_request.md)
- 💬 [Ask a Question](../../discussions)

---

---

## 👨‍💻 About the Developer

<div align="center">

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&pause=1000&color=2196F3&center=true&vCenter=true&width=435&lines=Full+Stack+Developer;Data+Analytics+Enthusiast;Fitness+Tech+Innovator" alt="Typing SVG" />

### 🌟 Sunil Sharma

**Passionate about creating innovative solutions for fitness data analysis**

[![GitHub Profile](https://img.shields.io/badge/GitHub-@sunbyte16-black?style=for-the-badge&logo=github&logoColor=white)](https://github.com/sunbyte16)
[![LinkedIn Profile](https://img.shields.io/badge/LinkedIn-Sunil%20Kumar-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/sunil-kumar-bb88bb31a/)
[![Portfolio Website](https://img.shields.io/badge/Portfolio-Visit%20Now-00D4AA?style=for-the-badge&logo=netlify&logoColor=white)](https://lively-dodol-cc397c.netlify.app)

</div>

---

<div align="center">

### 🚀 Project Stats

![GitHub repo size](https://img.shields.io/github/repo-size/sunbyte16/fitness-dashboard?style=flat-square)
![GitHub last commit](https://img.shields.io/github/last-commit/sunbyte16/fitness-dashboard?style=flat-square)
![GitHub issues](https://img.shields.io/github/issues/sunbyte16/fitness-dashboard?style=flat-square)
![GitHub pull requests](https://img.shields.io/github/issues-pr/sunbyte16/fitness-dashboard?style=flat-square)

**⚠️ Important Note**

This dashboard is designed for exploratory data analysis. For production use or sensitive data, implement appropriate security measures and data protection protocols.

---

**Created By❤️[Sunil Sharma](https://github.com/sunbyte16) for the fitness data community**

[![Star this repo](https://img.shields.io/github/stars/sunbyte16/fitness-dashboard?style=social)](https://github.com/sunbyte16/fitness-dashboard/stargazers)
[![Fork this repo](https://img.shields.io/github/forks/sunbyte16/fitness-dashboard?style=social)](https://github.com/sunbyte16/fitness-dashboard/network/members)
[![Follow on GitHub](https://img.shields.io/github/followers/sunbyte16?style=social)](https://github.com/sunbyte16)

</div>
#
