# Internal Backend ML

This repository contains the machine learning backend for our project. It is designed to handle model training, inference, and integration with other components of the system.

## Project Structure

- `/internal`: Directory for internal modules.
  - `/internal/models`: Implementation of data classes and request models.
    - `__init__.py`: Initialization file for the models module.
    - `data_class.py`: Script for data classes.
    - `request_model.py`: Script for request models.
  - `/internal/routers`: Implementation of API routes.
    - `__init__.py`: Initialization file for the routers module.
    - `internal.py`: Script for internal routes.
  - `/internal/services`: Implementation of service logic.
    - `__init__.py`: Initialization file for the services module.
    - `prediction_service.py`: Script for prediction service.
  - `/internal/utils`: Utility functions and helpers.
    - `__init__.py`: Initialization file for the utils module.
    - `data_preprocessing.py`: Script for data preprocessing.

## Technologies Used

- **Python**: Programming language for developing the backend.
- **Libraries**:
  - `pandas`: Data manipulation and analysis.
  - `numpy`: Numerical computing.
  - `matplotlib`: Plotting and visualization.
  - `seaborn`: Statistical data visualization.
- **Model**:
  - Linear Regression with Gradient Descent

## Integration with Other Components

This repository is part of a larger project with the following components:

- **Frontend**: [Frontend Repository](https://github.com/hackathon5-7/frontend)
- **External Backend**: [External Backend Repository](https://github.com/hackathon5-7/external-backend)
