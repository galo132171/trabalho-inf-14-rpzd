{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPoRk79d6s47mpWNpoKxPJm",
      "include_colab_link": true
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
        "<a href=\"https://colab.research.google.com/github/galo132171/trabalho-inf-14-rpzd/blob/main/aceler%C3%A7%C3%A3o%20e%20frenagem9Passos).py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "A ideia é a seguinte, fazer com que cada modelo de carro tenha acelerações e frenagens diferentes entre sí, os carros escolhidos foram a Dodge Ram, Civic, Palio e Ferrari, e caso o usuário não escolha um carro que existe no jogo, deverá mostrar \"Carro não encontrado\", com o tempo de 0 a 100 dos carros."
      ],
      "metadata": {
        "id": "BJlNnFtpFPV7"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "carros = {\n",
        "    \"Dodge ram\": {\"aceleracao\": 5.0, \"frenagem\": 7.0},\n",
        "    \"Civic\": {\"aceleracao\": 6.5, \"frenagem\": 9.0},\n",
        "    \"Palio\": {\"aceleracao\": 2.0, \"frenagem\": 6.0},\n",
        "    \"Ferrari\": {\"aceleracao\": 10.0, \"frenagem\": 13.0}\n",
        "}\n",
        "carro = input(\"Escolha o carro: \")\n",
        "if carro in carros:\n",
        "    aceleracao = carros[carro][\"aceleracao\"]\n",
        "    frenagem = carros[carro][\"frenagem\"]\n",
        "    tempo_0_100 = (100 / 3.6) / aceleracao\n",
        "    print(f\"\\n {carro}\")\n",
        "    print(f\"Aceleração: {aceleracao} m/s²\")\n",
        "    print(f\"Frenagem: {frenagem} m/s²\")\n",
        "    print(f\"Tempo de 0 a 100 km/h: {tempo_0_100:.2f} segundos\")\n",
        "else:\n",
        "    print(\"Carro não encontrado!\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "RNf9oyzuEQDa",
        "outputId": "aa67085c-6d82-427b-acd2-f8bf0faf80da"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Escolha o carro: Dodge ram\n",
            "\n",
            " Dodge ram\n",
            "Aceleração: 5.0 m/s²\n",
            "Frenagem: 7.0 m/s²\n",
            "Tempo de 0 a 100 km/h: 5.56 segundos\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "bp7S7hvBE7hz"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}