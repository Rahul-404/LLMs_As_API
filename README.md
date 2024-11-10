# **LLMs As API - Multimodal API with FastAPI and Langserve**

This project creates a multi-Language Model (LLM) system that allows you to switch between different LLMs for different routes using **FastAPI**. The API is designed to be extensible, allowing you to integrate and scale new LLMs as needed.

Additionally, the project includes a **Streamlit-based frontend** (`client.py`) to provide a user-friendly interface for interacting with the API.

### **Key Features**
- **FastAPI Backend** to serve multiple LLMs through different routes.
- **Langserve Integration** to manage the interaction with multiple LLMs.
- **Streamlit Frontend** to easily interact with the backend via a simple web-based interface.
- **Demo Video** showcasing the working of the project and how to interact with the API.

---

## **Table of Contents**

- [Installation](#installation)
- [Project Structure](#project-structure)
- [How to Run the Project](#how-to-run-the-project)
- [Routes and API Endpoints](#routes-and-api-endpoints)
- [Streamlit Frontend](#streamlit-frontend)
- [Project Demo Video](#project-demo-video)
- [Contributing](#contributing)
- [License](#license)

---

## **Installation**

To get started with this project, clone the repository and install the dependencies:

```bash
git clone https://github.com/Rahul-404/LLMs_As_API.git
cd LLMs_As_API
```

### Install dependencies:

```bash
# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install required Python packages
pip install -r requirements.txt
```

**Requirements**:
- **Python 3.8+**
- **FastAPI**
- **Langserve** (for handling LLMs)
- **Uvicorn** (for running the FastAPI server)
- **Streamlit** (for the frontend interface)
- **Other dependencies** listed in `requirements.txt`

---

## **Project Structure**

The project is organized as follows:

```
LLMs_As_API/
│
├── assets/             # directory contains assets used
├── app.py              # FastAPI application serving routes
├── client.py           # Streamlit-based frontend to interact with the API
├── intoroduction.ipynb # Project overview
├── requirements.txt    # List of required Python packages
└── README.md           # Project documentation
```

- `**app.py**`: Contains FastAPI routes and logic for interacting with different LLMs using Langserve.
- `**client.py**`: The **Streamlit-based frontend** to interact with the API.

---

## **How to Run the Project**

### 1. **Run the Backend (FastAPI)**

In the root project directory, you can start the FastAPI app by simply running:

```bash
python app.py
```

This will run the FastAPI server locally at `http://127.0.0.1:8000`.

### 2. **Run the Streamlit Frontend (client.py)**

Once the backend is running, you can start the Streamlit-based frontend by running the following command:

```bash
streamlit run client.py
```

This will open a Streamlit app in your browser, typically at `http://localhost:8501`.

### 3. **Access API Documentation**

FastAPI automatically generates interactive documentation. You can view it by navigating to the following URL:

```
http://127.0.0.1:8000/docs
```

Here you can test different routes and see how to interact with the API.

---

## **Routes and API Endpoints**

The backend exposes two main routes for generating different types of text:

- **POST `/essay/invoke`**: Generates an essay based on a given topic.
  - **Parameters**:
    - `input.topic` (str): The topic for the essay.
  - **Response**: The generated essay text.
  
  Example Request:

  ```bash
  POST http://127.0.0.1:8000/essay/invoke
  {
    "input": {
      "topic": "The Impact of Climate Change"
    }
  }
  ```

  Response Example:

  ```json
  {
    "output": "The impact of climate change is a critical issue..."
  }
  ```

- **POST `/poem/invoke`**: Generates a poem based on a given topic.
  - **Parameters**:
    - `input.topic` (str): The topic for the poem.
  - **Response**: The generated poem text.

  Example Request:

  ```bash
  POST http://127.0.0.1:8000/poem/invoke
  {
    "input": {
      "topic": "The Beauty of Nature"
    }
  }
  ```

  Response Example:

  ```json
  {
    "output": "Nature's beauty lies in the trees..."
  }
  ```

---

## **Streamlit Frontend**

The `client.py` script uses **Streamlit** to create an easy-to-use frontend to interact with the API. The app allows you to:
- Enter a topic for an essay and generate the essay by sending a request to the `/essay/invoke` endpoint.
- Enter a topic for a poem and generate the poem by sending a request to the `/poem/invoke` endpoint.
- View the response returned by the API directly on the Streamlit interface.

### How to Use:
1. Run the Streamlit app by executing:
   ```bash
   streamlit run client.py
   ```
2. Open the app in your browser (`http://localhost:8501` by default).
3. Enter a topic in the **"Write an essay on"** field, and the app will call the `/essay/invoke` endpoint to generate an essay.
4. Enter a topic in the **"Write a poem on"** field, and the app will call the `/poem/invoke` endpoint to generate a poem.
5. The essay or poem generated by the LLM will be displayed below the respective input field.

---

## **Project Demo Video**

To provide an overview of how this project works, we've included a **demo video**. This video demonstrates how to:
- Set up the FastAPI server.
- Interact with the backend using the **Streamlit frontend**.
- Generate essays and poems by selecting a topic.

### **How to Watch the Demo Video**:
1. Open the video below to see a full demonstration of how the system works.
2. The video will explain:
   - Setting up the FastAPI server.
   - How to use the Streamlit-based frontend.
   - Sending requests to generate essays and poems.

   **You can view the video here:**

   - [Project Demo Video](path/to/your-demo-video.mp4) *(replace with your actual video link or local file path)*

> **Note**: Please ensure you have the necessary software installed (like a video player or browser) to watch the video.

---

## **Contributing**

We welcome contributions! If you'd like to contribute to this project, feel free to submit a pull request with your proposed changes. 

Please ensure you follow these steps before submitting:
- Fork the repository.
- Clone your forked repository to your local machine.
- Create a new branch for your feature or bugfix.
- Test your changes locally.
- Commit your changes and push them to your fork.
- Open a pull request with a detailed description of the changes.

---

## **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
