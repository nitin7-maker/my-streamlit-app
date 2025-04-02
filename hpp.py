{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMYjmBMZLC5YkqlYvFDVtFl",
      "include_colab_link": True
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/MYoussef885/House_Price_Prediction/blob/main/House_Price_Prediction.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "NxlXx8zIIxy-"
      },
      "outputs": [],
      "source": [
        "import numpy as np\n",
        "import pandas as pd\n",
        "import matplotlib.pyplot as plt\n",
        "import seaborn as sns\n",
        "import sklearn.datasets\n",
        "from sklearn.model_selection import train_test_split\n",
        "from xgboost import XGBRegressor\n",
        "from sklearn import metrics"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Importing the Boston House Price Dataset"
      ],
      "metadata": {
        "id": "KF0NACJfKdZr"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "house_price_dataset = sklearn.datasets.fetch_california_housing()"
      ],
      "metadata": {
        "id": "k6c8SqjtKNv7"
      },
      "execution_count": 3,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(house_price_dataset)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "p_aMus38Kyb4",
        "outputId": "5d491c92-2a63-455c-cc0f-5206c2d02d14"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{'data': array([[   8.3252    ,   41.        ,    6.98412698, ...,    2.55555556,\n",
            "          37.88      , -122.23      ],\n",
            "       [   8.3014    ,   21.        ,    6.23813708, ...,    2.10984183,\n",
            "          37.86      , -122.22      ],\n",
            "       [   7.2574    ,   52.        ,    8.28813559, ...,    2.80225989,\n",
            "          37.85      , -122.24      ],\n",
            "       ...,\n",
            "       [   1.7       ,   17.        ,    5.20554273, ...,    2.3256351 ,\n",
            "          39.43      , -121.22      ],\n",
            "       [   1.8672    ,   18.        ,    5.32951289, ...,    2.12320917,\n",
            "          39.43      , -121.32      ],\n",
            "       [   2.3886    ,   16.        ,    5.25471698, ...,    2.61698113,\n",
            "          39.37      , -121.24      ]]), 'target': array([4.526, 3.585, 3.521, ..., 0.923, 0.847, 0.894]), 'frame': None, 'target_names': ['MedHouseVal'], 'feature_names': ['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup', 'Latitude', 'Longitude'], 'DESCR': '.. _california_housing_dataset:\\n\\nCalifornia Housing dataset\\n--------------------------\\n\\n**Data Set Characteristics:**\\n\\n    :Number of Instances: 20640\\n\\n    :Number of Attributes: 8 numeric, predictive attributes and the target\\n\\n    :Attribute Information:\\n        - MedInc        median income in block group\\n        - HouseAge      median house age in block group\\n        - AveRooms      average number of rooms per household\\n        - AveBedrms     average number of bedrooms per household\\n        - Population    block group population\\n        - AveOccup      average number of household members\\n        - Latitude      block group latitude\\n        - Longitude     block group longitude\\n\\n    :Missing Attribute Values: None\\n\\nThis dataset was obtained from the StatLib repository.\\nhttps://www.dcc.fc.up.pt/~ltorgo/Regression/cal_housing.html\\n\\nThe target variable is the median house value for California districts,\\nexpressed in hundreds of thousands of dollars ($100,000).\\n\\nThis dataset was derived from the 1990 U.S. census, using one row per census\\nblock group. A block group is the smallest geographical unit for which the U.S.\\nCensus Bureau publishes sample data (a block group typically has a population\\nof 600 to 3,000 people).\\n\\nA household is a group of people residing within a home. Since the average\\nnumber of rooms and bedrooms in this dataset are provided per household, these\\ncolumns may take surprisingly large values for block groups with few households\\nand many empty houses, such as vacation resorts.\\n\\nIt can be downloaded/loaded using the\\n:func:`sklearn.datasets.fetch_california_housing` function.\\n\\n.. topic:: References\\n\\n    - Pace, R. Kelley and Ronald Barry, Sparse Spatial Autoregressions,\\n      Statistics and Probability Letters, 33 (1997) 291-297\\n'}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Loading the dataset to a pandas dataframe\n",
        "house_price_dataframe = pd.DataFrame(house_price_dataset.data, columns = house_price_dataset.feature_names)\n"
      ],
      "metadata": {
        "id": "gsCsZQ27LJgM"
      },
      "execution_count": 6,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "house_price_dataframe.head()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "0QMscwYcMUdI",
        "outputId": "f018b965-4733-45e9-bda0-08a366c07921"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "   MedInc  HouseAge  AveRooms  ...  AveOccup  Latitude  Longitude\n",
              "0  8.3252      41.0  6.984127  ...  2.555556     37.88    -122.23\n",
              "1  8.3014      21.0  6.238137  ...  2.109842     37.86    -122.22\n",
              "2  7.2574      52.0  8.288136  ...  2.802260     37.85    -122.24\n",
              "3  5.6431      52.0  5.817352  ...  2.547945     37.85    -122.25\n",
              "4  3.8462      52.0  6.281853  ...  2.181467     37.85    -122.25\n",
              "\n",
              "[5 rows x 8 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-8f628791-3556-4010-91b7-d9440ded5ef1\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>MedInc</th>\n",
              "      <th>HouseAge</th>\n",
              "      <th>AveRooms</th>\n",
              "      <th>AveBedrms</th>\n",
              "      <th>Population</th>\n",
              "      <th>AveOccup</th>\n",
              "      <th>Latitude</th>\n",
              "      <th>Longitude</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>8.3252</td>\n",
              "      <td>41.0</td>\n",
              "      <td>6.984127</td>\n",
              "      <td>1.023810</td>\n",
              "      <td>322.0</td>\n",
              "      <td>2.555556</td>\n",
              "      <td>37.88</td>\n",
              "      <td>-122.23</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>8.3014</td>\n",
              "      <td>21.0</td>\n",
              "      <td>6.238137</td>\n",
              "      <td>0.971880</td>\n",
              "      <td>2401.0</td>\n",
              "      <td>2.109842</td>\n",
              "      <td>37.86</td>\n",
              "      <td>-122.22</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>7.2574</td>\n",
              "      <td>52.0</td>\n",
              "      <td>8.288136</td>\n",
              "      <td>1.073446</td>\n",
              "      <td>496.0</td>\n",
              "      <td>2.802260</td>\n",
              "      <td>37.85</td>\n",
              "      <td>-122.24</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>5.6431</td>\n",
              "      <td>52.0</td>\n",
              "      <td>5.817352</td>\n",
              "      <td>1.073059</td>\n",
              "      <td>558.0</td>\n",
              "      <td>2.547945</td>\n",
              "      <td>37.85</td>\n",
              "      <td>-122.25</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>3.8462</td>\n",
              "      <td>52.0</td>\n",
              "      <td>6.281853</td>\n",
              "      <td>1.081081</td>\n",
              "      <td>565.0</td>\n",
              "      <td>2.181467</td>\n",
              "      <td>37.85</td>\n",
              "      <td>-122.25</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-8f628791-3556-4010-91b7-d9440ded5ef1')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-8f628791-3556-4010-91b7-d9440ded5ef1 button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-8f628791-3556-4010-91b7-d9440ded5ef1');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-586ff32e-6105-4859-9926-e43b759f4d46\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-586ff32e-6105-4859-9926-e43b759f4d46')\"\n",
              "            title=\"Suggest charts.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-586ff32e-6105-4859-9926-e43b759f4d46 button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "    </div>\n",
              "  </div>\n"
            ]
          },
          "metadata": {},
          "execution_count": 8
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# add the target column to the dataframe\n",
        "house_price_dataframe['price'] = house_price_dataset.target"
      ],
      "metadata": {
        "id": "0jVZmCcCMva4"
      },
      "execution_count": 9,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "house_price_dataframe.head()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "JTSiwIMWNJNS",
        "outputId": "e400f513-3d96-42f3-b0c0-60d1da9b0dd8"
      },
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "   MedInc  HouseAge  AveRooms  AveBedrms  ...  AveOccup  Latitude  Longitude  price\n",
              "0  8.3252      41.0  6.984127   1.023810  ...  2.555556     37.88    -122.23  4.526\n",
              "1  8.3014      21.0  6.238137   0.971880  ...  2.109842     37.86    -122.22  3.585\n",
              "2  7.2574      52.0  8.288136   1.073446  ...  2.802260     37.85    -122.24  3.521\n",
              "3  5.6431      52.0  5.817352   1.073059  ...  2.547945     37.85    -122.25  3.413\n",
              "4  3.8462      52.0  6.281853   1.081081  ...  2.181467     37.85    -122.25  3.422\n",
              "\n",
              "[5 rows x 9 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-7fd6a3e2-4a4d-440d-b677-b5fa3958ea92\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>MedInc</th>\n",
              "      <th>HouseAge</th>\n",
              "      <th>AveRooms</th>\n",
              "      <th>AveBedrms</th>\n",
              "      <th>Population</th>\n",
              "      <th>AveOccup</th>\n",
              "      <th>Latitude</th>\n",
              "      <th>Longitude</th>\n",
              "      <th>price</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>8.3252</td>\n",
              "      <td>41.0</td>\n",
              "      <td>6.984127</td>\n",
              "      <td>1.023810</td>\n",
              "      <td>322.0</td>\n",
              "      <td>2.555556</td>\n",
              "      <td>37.88</td>\n",
              "      <td>-122.23</td>\n",
              "      <td>4.526</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>8.3014</td>\n",
              "      <td>21.0</td>\n",
              "      <td>6.238137</td>\n",
              "      <td>0.971880</td>\n",
              "      <td>2401.0</td>\n",
              "      <td>2.109842</td>\n",
              "      <td>37.86</td>\n",
              "      <td>-122.22</td>\n",
              "      <td>3.585</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>7.2574</td>\n",
              "      <td>52.0</td>\n",
              "      <td>8.288136</td>\n",
              "      <td>1.073446</td>\n",
              "      <td>496.0</td>\n",
              "      <td>2.802260</td>\n",
              "      <td>37.85</td>\n",
              "      <td>-122.24</td>\n",
              "      <td>3.521</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>5.6431</td>\n",
              "      <td>52.0</td>\n",
              "      <td>5.817352</td>\n",
              "      <td>1.073059</td>\n",
              "      <td>558.0</td>\n",
              "      <td>2.547945</td>\n",
              "      <td>37.85</td>\n",
              "      <td>-122.25</td>\n",
              "      <td>3.413</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>3.8462</td>\n",
              "      <td>52.0</td>\n",
              "      <td>6.281853</td>\n",
              "      <td>1.081081</td>\n",
              "      <td>565.0</td>\n",
              "      <td>2.181467</td>\n",
              "      <td>37.85</td>\n",
              "      <td>-122.25</td>\n",
              "      <td>3.422</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-7fd6a3e2-4a4d-440d-b677-b5fa3958ea92')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-7fd6a3e2-4a4d-440d-b677-b5fa3958ea92 button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-7fd6a3e2-4a4d-440d-b677-b5fa3958ea92');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-f10a6bb2-310e-4365-ada6-96b8cc769491\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-f10a6bb2-310e-4365-ada6-96b8cc769491')\"\n",
              "            title=\"Suggest charts.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-f10a6bb2-310e-4365-ada6-96b8cc769491 button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "    </div>\n",
              "  </div>\n"
            ]
          },
          "metadata": {},
          "execution_count": 10
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# checking the number of rows and columns in the dataframe\n",
        "house_price_dataframe.shape"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "bV44-OLJNOzz",
        "outputId": "fc754423-7845-438b-b77d-b1762654a57b"
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(20640, 9)"
            ]
          },
          "metadata": {},
          "execution_count": 11
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# check for missing values\n",
        "house_price_dataframe.isnull().sum"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "IdA-5PW1Nc5q",
        "outputId": "6ba57f8b-2377-42d8-96a6-07c03652fee4"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<bound method NDFrame._add_numeric_operations.<locals>.sum of        MedInc  HouseAge  AveRooms  ...  Latitude  Longitude  price\n",
              "0       False     False     False  ...     False      False  False\n",
              "1       False     False     False  ...     False      False  False\n",
              "2       False     False     False  ...     False      False  False\n",
              "3       False     False     False  ...     False      False  False\n",
              "4       False     False     False  ...     False      False  False\n",
              "...       ...       ...       ...  ...       ...        ...    ...\n",
              "20635   False     False     False  ...     False      False  False\n",
              "20636   False     False     False  ...     False      False  False\n",
              "20637   False     False     False  ...     False      False  False\n",
              "20638   False     False     False  ...     False      False  False\n",
              "20639   False     False     False  ...     False      False  False\n",
              "\n",
              "[20640 rows x 9 columns]>"
            ]
          },
          "metadata": {},
          "execution_count": 12
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# statistical measures of the dataset\n",
        "house_price_dataframe.describe()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 300
        },
        "id": "Dlhhvm73NuXM",
        "outputId": "aaaed7e6-d9bf-4805-8ac9-e8a925e684e2"
      },
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "             MedInc      HouseAge  ...     Longitude         price\n",
              "count  20640.000000  20640.000000  ...  20640.000000  20640.000000\n",
              "mean       3.870671     28.639486  ...   -119.569704      2.068558\n",
              "std        1.899822     12.585558  ...      2.003532      1.153956\n",
              "min        0.499900      1.000000  ...   -124.350000      0.149990\n",
              "25%        2.563400     18.000000  ...   -121.800000      1.196000\n",
              "50%        3.534800     29.000000  ...   -118.490000      1.797000\n",
              "75%        4.743250     37.000000  ...   -118.010000      2.647250\n",
              "max       15.000100     52.000000  ...   -114.310000      5.000010\n",
              "\n",
              "[8 rows x 9 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-c5bf6e21-1a7e-4bc4-ab2e-745186cfe10a\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>MedInc</th>\n",
              "      <th>HouseAge</th>\n",
              "      <th>AveRooms</th>\n",
              "      <th>AveBedrms</th>\n",
              "      <th>Population</th>\n",
              "      <th>AveOccup</th>\n",
              "      <th>Latitude</th>\n",
              "      <th>Longitude</th>\n",
              "      <th>price</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>count</th>\n",
              "      <td>20640.000000</td>\n",
              "      <td>20640.000000</td>\n",
              "      <td>20640.000000</td>\n",
              "      <td>20640.000000</td>\n",
              "      <td>20640.000000</td>\n",
              "      <td>20640.000000</td>\n",
              "      <td>20640.000000</td>\n",
              "      <td>20640.000000</td>\n",
              "      <td>20640.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>mean</th>\n",
              "      <td>3.870671</td>\n",
              "      <td>28.639486</td>\n",
              "      <td>5.429000</td>\n",
              "      <td>1.096675</td>\n",
              "      <td>1425.476744</td>\n",
              "      <td>3.070655</td>\n",
              "      <td>35.631861</td>\n",
              "      <td>-119.569704</td>\n",
              "      <td>2.068558</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>std</th>\n",
              "      <td>1.899822</td>\n",
              "      <td>12.585558</td>\n",
              "      <td>2.474173</td>\n",
              "      <td>0.473911</td>\n",
              "      <td>1132.462122</td>\n",
              "      <td>10.386050</td>\n",
              "      <td>2.135952</td>\n",
              "      <td>2.003532</td>\n",
              "      <td>1.153956</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>min</th>\n",
              "      <td>0.499900</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.846154</td>\n",
              "      <td>0.333333</td>\n",
              "      <td>3.000000</td>\n",
              "      <td>0.692308</td>\n",
              "      <td>32.540000</td>\n",
              "      <td>-124.350000</td>\n",
              "      <td>0.149990</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>25%</th>\n",
              "      <td>2.563400</td>\n",
              "      <td>18.000000</td>\n",
              "      <td>4.440716</td>\n",
              "      <td>1.006079</td>\n",
              "      <td>787.000000</td>\n",
              "      <td>2.429741</td>\n",
              "      <td>33.930000</td>\n",
              "      <td>-121.800000</td>\n",
              "      <td>1.196000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>50%</th>\n",
              "      <td>3.534800</td>\n",
              "      <td>29.000000</td>\n",
              "      <td>5.229129</td>\n",
              "      <td>1.048780</td>\n",
              "      <td>1166.000000</td>\n",
              "      <td>2.818116</td>\n",
              "      <td>34.260000</td>\n",
              "      <td>-118.490000</td>\n",
              "      <td>1.797000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>75%</th>\n",
              "      <td>4.743250</td>\n",
              "      <td>37.000000</td>\n",
              "      <td>6.052381</td>\n",
              "      <td>1.099526</td>\n",
              "      <td>1725.000000</td>\n",
              "      <td>3.282261</td>\n",
              "      <td>37.710000</td>\n",
              "      <td>-118.010000</td>\n",
              "      <td>2.647250</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>max</th>\n",
              "      <td>15.000100</td>\n",
              "      <td>52.000000</td>\n",
              "      <td>141.909091</td>\n",
              "      <td>34.066667</td>\n",
              "      <td>35682.000000</td>\n",
              "      <td>1243.333333</td>\n",
              "      <td>41.950000</td>\n",
              "      <td>-114.310000</td>\n",
              "      <td>5.000010</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-c5bf6e21-1a7e-4bc4-ab2e-745186cfe10a')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-c5bf6e21-1a7e-4bc4-ab2e-745186cfe10a button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-c5bf6e21-1a7e-4bc4-ab2e-745186cfe10a');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-b3cf089e-ef8f-4fa4-909f-12d4ee1cf444\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-b3cf089e-ef8f-4fa4-909f-12d4ee1cf444')\"\n",
              "            title=\"Suggest charts.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-b3cf089e-ef8f-4fa4-909f-12d4ee1cf444 button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "    </div>\n",
              "  </div>\n"
            ]
          },
          "metadata": {},
          "execution_count": 13
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Understanding the **correlation** between various features in the dataset"
      ],
      "metadata": {
        "id": "_4_WnRTfOJAB"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "1. Positive Correlation\n",
        "2. Negative Correlation"
      ],
      "metadata": {
        "id": "m_qDVyB2ORPv"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "correlation = house_price_dataframe.corr()"
      ],
      "metadata": {
        "id": "INlW8yk2N8uL"
      },
      "execution_count": 18,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# constructing a heatmap to understand the correlation\n",
        "\n",
        "plt.figure(figsize=(10,10))\n",
        "sns.heatmap(correlation, cbar=True, square=True, fmt='.1f', annot=True, annot_kws={'size':8}, cmap='Blues')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 842
        },
        "id": "6hjfWdsmQ3Q7",
        "outputId": "4fc2d22d-5d6f-4787-92af-0f4feaf782cc"
      },
      "execution_count": 20,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<Axes: >"
            ]
          },
          "metadata": {},
          "execution_count": 20
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 1000x1000 with 2 Axes>"
            ],
            "image/png": "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+aWXbamgJOUWl+nU2SJ1blBHP508q3bhvjpbWGJWKihJu8/kaELvhlq9P105RWXq0chfu5KyL7DVmqlxt35q3O3c+eTMvm06vu17NY7ur1O7NsrzAueTBu17ae3Mx9RmYJY8fP11eOM3atipdh07l4pqQcdy0UnWV199paysLN19992qU6eO2XO33nqr4uPjdd9992nkyJGaO3euDhw4oO+//97UxtfXV1OmTNGkSZNUXl6u3r176+zZs9q4caP8/Px05513mtpmZGQoOTlZpaWl+vnnn/Xmm2+qb9++8vOrvNjz+eef10MPPaQ6deooNjZWRUVF2rZtm7KysjR58mSNHDlSTz75pO655x5NnTpVx44du2DCYw3PPPOMOnfubJp2/quvvlKrVq2qbX/WEj3iQSV+OEN7V38iVw8vdR81yfTc5kVvqkHbaDVo112lxYX68oV7VV5aopKCfH3+1Gg17nqNOg4aY7/gq0H3kQ9q48IZ+nn1J3Lz8FLPO871x6aP3lREu2hF/N4fK567V2W/98eyaaPVpNs16jR4jP2CrwYPvvmt5k25To+N6K7s/GL93+uVM2q+MylGKxMPaeXmw5r75U61iAjU1rljVFJarpSsPE1481s7R1593npyuAZe2UahQX768p0HlJtXpCsGPa93nhmplet/1sr1P+tYUoZenLNS696vHK3+YftBvffZBjtHXr04l1hqP+R+7Vzypg6u/VQuHl7qOPwh03O7lr6lsDbdFHZFtLyDwtQyZoQ2zH5ckhTc9ApF9oi1V9jV5qPtpzWmW31d1ypYBSXl+uCnytsf3NG5nvacztHuMzlyczboxdhmcnE2yNPVSf+6vrk2Hzdq+S+pdo6+eny6O1kjOoarX7MgFZWWacnOyhHNoe3DtDc5V3tTcpWZX6LVv6VrQu/KKcwPp+dr03GjHaOufl2GPaiti2bo128rzyfdbp9oem7r4lmq3zZa9dtGyyc4TFdcN1JrZ1TOVlq3WVs17WU5Cy5gL4aKi7zL74033qjy8nKtXLnS4rmtW7cqOjpau3fvlqurq1q3bq3IyEgdPXrU7CK8iooKzZo1S3PmzNGRI0fk7++vTp06adq0abrqqqt07NgxNW7c2NTe2dlZ4eHhGjhwoF5++WWFhJwbBl68eLH+/e9/69dff5W3t7fatm2riRMnmmYy3Lx5s+67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ZJaDetuJEydw7949nDp1ChUrVkSDBg0wf/58/PDDD5gzZ450Qr2PUeg6WSXFy8sLjx49QnZ2Np4/f46AgACYm5sLHYuIiIiIiN6Rk5ODtLQ0mZ+cnJz/9JqXL1+GiYmJtMACiiatU1NTw9WrVz/4u9u3b4eFhQXq1q2L6dOnIzMzU+Z169WrJ53FHADat2+PtLQ03L1795Pzlckii4iIiIiIygZfX18YGxvL/Pj6+n78Fz8gPj4eFSrIrmeqoaEBMzMzxMfHv/f3+vbti23btuHs2bOYPn06tm7div79+8u87tsFFgDp4w+97rvKZLsgERERERH9Q5m7BadPn46JEyfKbHt3zdg3pk2bhp9++umDr3f//v1/nWX48OHS/12vXj1YW1vDw8MDERERJTq/A4ssIiIiIiIqNdra2u8tqt41adIkeHt7f3AfBwcHWFlZ4eXLlzLb8/LykJyc/N77rYrj6uoKANJZyq2srHDt2jWZfRISitZ1/JzXZZFFRERERERKwdLSEpaWlh/dz83NDampqbhx4wYaN24MADhz5gwKCgqkhdOnCAsLAwBYW1tLX3fhwoV4+fKltB3x5MmTMDIyQu3atT/5dXlPFhERERFRWSdS4p9SUKtWLXh6emLYsGG4du0agoODMXr0aPTu3Vs6s2BsbCxq1qwpHZmKiIjA/PnzcePGDURGRuLQoUPw8vJCy5Yt4ezsDABo164dateujQEDBiA8PBx//fUXZs6ciVGjRn3yaBzAIouIiIiIiMqg7du3o2bNmvDw8EDHjh3RvHlzbNiwQfq8RCLBw4cPpbMHamlp4dSpU2jXrh1q1qyJSZMmoWfPnjh8+LD0d9TV1fHnn39CXV0dbm5u6N+/P7y8vGTW1foUbBckIiIiIqIyx8zM7IMLD9vZ2aGwsFD62NbWFkFBQR993apVq+Lo0aP/KRuLLCIiIiKiMk6k1PMLqh62CxIREREREZUgFllEREREREQliO2CRERERERlnIjdgkqFI1lEREREREQliEUWERERERFRCWK7IBERERFRGcduQeXCkSwiIiIiIqISxCKLiIiIiIioBLFdkIiIiIiorGO/oFLhSBYREREREVEJYpFFRERERERUgtguSERERERUxonYL6hUOJJFRERERERUglhkERERERERlSC2CxIRERERlXEidgsqFY5kERERERERlSAWWURERERERCWI7YJERERERGUcuwWVi6iwsLBQ6BAEmPTbJnQEpdPta2ehIyid7Nx8oSMonepWBkJHUDp5+bys08dZG2sKHUHpJIrzhI6gVJZM+0XoCEon6+ZqoSO8153nYqEjvFfdyqr3Xs12QSIiIiIiohLEdkEiIiIiorKO/YJKhSNZREREREREJYhFFhERERERUQliuyARERERURknYr+gUuFIFhERERERUQlikUVERERERFSC2C5IRERERFTGidgtqFQ4kkVERERERFSCWGQRERERERGVILYLEhERERGVcewWVC4cySIiIiIiIipBLLKIiIiIiIhKENsFiYiIiIjKOvYLKhWOZBEREREREZUgFllEREREREQliO2CRERERERlnIj9gkqFI1lEREREREQliEUWERERERFRCWK7IBERERFRGSdit6BS4UgWERERERFRCWKRRUREREREVILYLkhEREREVMaxW1C5cCSLiIiIiIioBLHIIiIiIiIiKkFsFyQiIiIiKuvYL6hUOJJFRERERERUglhkvSMyMhIikQhhYWFCRyEiIiIiojKI7YLvsLW1RVxcHCwsLISOQkRERET0SUTsF1QqLLLekpubCy0tLVhZWQkdpdQ5VDTE2v81g7mhNtIyJRi5/hIexL6W2adfSwf8z7Om9LGNmR4uPXiJASvOKzquQlQ00MLQprYw1NZApiQfG6/E4EVajsw+FvqaGOpqiyqmuniVkYtZxx8LlLb0WRlqY2TzKtLjsTY4Gs9Ts2X2qWNlgD6NbaCjoYZCADefp2HnjRcoFCayQqS/jMXVbcuRk5EGTV19uPYbD2PrqsXu+/TyCdw/9QcKCwpRsbozGvcaCTX18nfZTU98gZAdy5GbkQZNHT006TMeRu85Js+unMDD03uAwkJYOjmj4TcjeExU5JikJsTi1MalyBKnQVtXDx5DJsG8kp3cfmmv4nHK3w+voiNgZGGF3nN/VXxYBeH15B9+U79Bpy/roaqNOVy/88WtR7HF7jewmxsmD2oLNZEI564/wjjf35GXV6DgtEQfV67bBVu1aoXRo0dj9OjRMDY2hoWFBXx8fFBYWPQR0M7ODvPnz4eXlxeMjIwwfPjwYtsF7969i6+//hpGRkYwNDREixYtEBERIX1+48aNqFWrFnR0dFCzZk38+qvyvyGsGOKKwLOP0WTy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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Splitting the data and target"
      ],
      "metadata": {
        "id": "PW-ozm6ugVec"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "X = house_price_dataframe.drop(['price'], axis=1)\n",
        "Y = house_price_dataframe['price']"
      ],
      "metadata": {
        "id": "OG-1ekOyRZ17"
      },
      "execution_count": 22,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(X,Y)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "GEAZFIxZgx-T",
        "outputId": "d7f40f9b-a3a8-4519-da59-113457094437"
      },
      "execution_count": 23,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "       MedInc  HouseAge  AveRooms  ...  AveOccup  Latitude  Longitude\n",
            "0      8.3252      41.0  6.984127  ...  2.555556     37.88    -122.23\n",
            "1      8.3014      21.0  6.238137  ...  2.109842     37.86    -122.22\n",
            "2      7.2574      52.0  8.288136  ...  2.802260     37.85    -122.24\n",
            "3      5.6431      52.0  5.817352  ...  2.547945     37.85    -122.25\n",
            "4      3.8462      52.0  6.281853  ...  2.181467     37.85    -122.25\n",
            "...       ...       ...       ...  ...       ...       ...        ...\n",
            "20635  1.5603      25.0  5.045455  ...  2.560606     39.48    -121.09\n",
            "20636  2.5568      18.0  6.114035  ...  3.122807     39.49    -121.21\n",
            "20637  1.7000      17.0  5.205543  ...  2.325635     39.43    -121.22\n",
            "20638  1.8672      18.0  5.329513  ...  2.123209     39.43    -121.32\n",
            "20639  2.3886      16.0  5.254717  ...  2.616981     39.37    -121.24\n",
            "\n",
            "[20640 rows x 8 columns] 0        4.526\n",
            "1        3.585\n",
            "2        3.521\n",
            "3        3.413\n",
            "4        3.422\n",
            "         ...  \n",
            "20635    0.781\n",
            "20636    0.771\n",
            "20637    0.923\n",
            "20638    0.847\n",
            "20639    0.894\n",
            "Name: price, Length: 20640, dtype: float64\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Splitting the data into training data and test data"
      ],
      "metadata": {
        "id": "PiibjUFeg60p"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.2, random_state=2)"
      ],
      "metadata": {
        "id": "CmQ0u3VRgzrP"
      },
      "execution_count": 24,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(X.shape, X_train.shape, X_test.shape)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Zvt65MUWhrHh",
        "outputId": "752f1c3d-817d-42c2-fd02-b241a86482b2"
      },
      "execution_count": 25,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "(20640, 8) (16512, 8) (4128, 8)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Model Training"
      ],
      "metadata": {
        "id": "QGOIdaw0iEiu"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "XGBoost Regressor"
      ],
      "metadata": {
        "id": "Cz7W0nqhiIWC"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# load the model\n",
        "model = XGBRegressor()"
      ],
      "metadata": {
        "id": "QI5w4CLFhyv2"
      },
      "execution_count": 26,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#training the model with X_train\n",
        "model.fit(X_train, Y_train)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 248
        },
        "id": "EMM8-waOiqMn",
        "outputId": "14abe134-2653-4dd0-da02-944fda628a19"
      },
      "execution_count": 27,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "XGBRegressor(base_score=None, booster=None, callbacks=None,\n",
              "             colsample_bylevel=None, colsample_bynode=None,\n",
              "             colsample_bytree=None, early_stopping_rounds=None,\n",
              "             enable_categorical=False, eval_metric=None, feature_types=None,\n",
              "             gamma=None, gpu_id=None, grow_policy=None, importance_type=None,\n",
              "             interaction_constraints=None, learning_rate=None, max_bin=None,\n",
              "             max_cat_threshold=None, max_cat_to_onehot=None,\n",
              "             max_delta_step=None, max_depth=None, max_leaves=None,\n",
              "             min_child_weight=None, missing=nan, monotone_constraints=None,\n",
              "             n_estimators=100, n_jobs=None, num_parallel_tree=None,\n",
              "             predictor=None, random_state=None, ...)"
            ],
            "text/html": [
              "<style>#sk-container-id-1 {color: black;background-color: white;}#sk-container-id-1 pre{padding: 0;}#sk-container-id-1 div.sk-toggleable {background-color: white;}#sk-container-id-1 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-1 label.sk-toggleable__label-arrow:before {content: \"▸\";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-1 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-1 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-1 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-1 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-1 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-1 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: \"▾\";}#sk-container-id-1 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-1 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-1 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-1 div.sk-parallel-item::after {content: \"\";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-1 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-serial::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-1 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-1 div.sk-item {position: relative;z-index: 1;}#sk-container-id-1 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-1 div.sk-item::before, #sk-container-id-1 div.sk-parallel-item::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-1 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-1 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-1 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-1 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-1 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-1 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-1 div.sk-label-container {text-align: center;}#sk-container-id-1 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-1 div.sk-text-repr-fallback {display: none;}</style><div id=\"sk-container-id-1\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>XGBRegressor(base_score=None, booster=None, callbacks=None,\n",
              "             colsample_bylevel=None, colsample_bynode=None,\n",
              "             colsample_bytree=None, early_stopping_rounds=None,\n",
              "             enable_categorical=False, eval_metric=None, feature_types=None,\n",
              "             gamma=None, gpu_id=None, grow_policy=None, importance_type=None,\n",
              "             interaction_constraints=None, learning_rate=None, max_bin=None,\n",
              "             max_cat_threshold=None, max_cat_to_onehot=None,\n",
              "             max_delta_step=None, max_depth=None, max_leaves=None,\n",
              "             min_child_weight=None, missing=nan, monotone_constraints=None,\n",
              "             n_estimators=100, n_jobs=None, num_parallel_tree=None,\n",
              "             predictor=None, random_state=None, ...)</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-1\" type=\"checkbox\" checked><label for=\"sk-estimator-id-1\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">XGBRegressor</label><div class=\"sk-toggleable__content\"><pre>XGBRegressor(base_score=None, booster=None, callbacks=None,\n",
              "             colsample_bylevel=None, colsample_bynode=None,\n",
              "             colsample_bytree=None, early_stopping_rounds=None,\n",
              "             enable_categorical=False, eval_metric=None, feature_types=None,\n",
              "             gamma=None, gpu_id=None, grow_policy=None, importance_type=None,\n",
              "             interaction_constraints=None, learning_rate=None, max_bin=None,\n",
              "             max_cat_threshold=None, max_cat_to_onehot=None,\n",
              "             max_delta_step=None, max_depth=None, max_leaves=None,\n",
              "             min_child_weight=None, missing=nan, monotone_constraints=None,\n",
              "             n_estimators=100, n_jobs=None, num_parallel_tree=None,\n",
              "             predictor=None, random_state=None, ...)</pre></div></div></div></div></div>"
            ]
          },
          "metadata": {},
          "execution_count": 27
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Evaluation"
      ],
      "metadata": {
        "id": "WVIAIL2Qi75r"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Prediction on training data"
      ],
      "metadata": {
        "id": "KcNqvEpHjGqO"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# accuracy for prediction on training data\n",
        "training_data_prediction = model.predict(X_train)"
      ],
      "metadata": {
        "id": "-qBFZAuSi1t3"
      },
      "execution_count": 28,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(training_data_prediction)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "5fNmbxhAjgD1",
        "outputId": "fb10a921-cd19-474b-a24d-5a87867bfc05"
      },
      "execution_count": 29,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[0.6893792  2.986824   0.48874274 ... 1.8632544  1.7800125  0.7565893 ]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# R Squared Error\n",
        "score_1 = metrics.r2_score(Y_train, training_data_prediction)\n",
        "\n",
        "# Mean Absolute Error\n",
        "score_2 = metrics.mean_absolute_error(Y_train, training_data_prediction)\n",
        "\n",
        "print('R Sqaured Error:', score_1)\n",
        "print('Mean Absolute Error:', score_2)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "MoRXGrVOjlc3",
        "outputId": "5131178c-c66d-4eb8-ea73-462c379037b6"
      },
      "execution_count": 30,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "R Sqaured Error: 0.9451221492760822\n",
            "Mean Absolute Error: 0.1919170860794262\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Visualize the actuale prices and predicted prices"
      ],
      "metadata": {
        "id": "0HXbIXMpl0Sh"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "plt.scatter(Y_train, training_data_prediction)\n",
        "plt.xlabel(\"Actual Price\")\n",
        "plt.ylabel(\"Predicted Price\")\n",
        "plt.title(\"Actual Price vs Predicted Price\")\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 472
        },
        "id": "AkX_8rbol6X6",
        "outputId": "cc88d8a9-8bcb-45ed-b985-420876d243bf"
      },
      "execution_count": 33,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Prediction on test data"
      ],
      "metadata": {
        "id": "YshfEu3WlNaf"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# accuracy for prediction on test data\n",
        "test_data_prediction = model.predict(X_test)"
      ],
      "metadata": {
        "id": "jKJotv_lkqPi"
      },
      "execution_count": 31,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# R Squared Error\n",
        "score_1 = metrics.r2_score(Y_test, test_data_prediction)\n",
        "\n",
        "# Mean Absolute Error\n",
        "score_2 = metrics.mean_absolute_error(Y_test, test_data_prediction)\n",
        "\n",
        "print('R Sqaured Error:', score_1)\n",
        "print('Mean Absolute Error:', score_2)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "QZIaQ0bZlYU8",
        "outputId": "ee10e939-0b09-4b82-d187-1a3687914457"
      },
      "execution_count": 32,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "R Sqaured Error: 0.8412904408180302\n",
            "Mean Absolute Error: 0.30753655785801337\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "3NA45vC_lj3Y"
      },
      "execution_count": None,
      "outputs": []
    }
  ]
}
