{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
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
        "<a href=\"https://colab.research.google.com/github/Galung29/ilp-hazard-simulator/blob/main/WAW.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8GVQWVuov6ED",
        "outputId": "3b16bba0-4209-4792-a9c1-cfa64b5a9230"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "RAW:\n",
            "R1 = 24\n",
            "R2 = 15\n",
            "R3 = 5\n"
          ]
        }
      ],
      "source": [
        "I1: R1 = 10\n",
        "I2: R2 = R1 + 5\n",
        "I3: R3 = R2 * 2\n",
        "\n",
        "print(\"RAW:\")\n",
        "print(\"R1 =\", R1)\n",
        "print(\"R2 =\", R2)\n",
        "print(\"R3 =\", R3)"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Implementasi WAR (Write-After-Read)\n",
        "# I1 membaca R1, kemudian I2 menulis ke R1\n",
        "\n",
        "I1 = \"R1 = 10\"  # Misalkan I1 membaca atau menggunakan nilai awal R1\n",
        "I2 = \"R1 = R2 + 5\" # I2 menulis ulang nilai ke R1\n",
        "\n",
        "# Simulasi nilai\n",
        "R2 = 50\n",
        "R1 = 10         # Dibaca oleh instruksi sebelumnya\n",
        "R1 = R2 + 90     # Menimpa R1 (terjadi WAR hazard)\n",
        "\n",
        "print(\"WAR:\")\n",
        "print(\"R1 =\", R1)\n",
        "print(\"R2 =\", R2)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "N3Q3Z6w5aPvA",
        "outputId": "962fceed-4d90-4bb8-cd64-999ae430debd"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "WAR:\n",
            "R1 = 140\n",
            "R2 = 50\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Implementasi WAW (Write-After-Write)\n",
        "# I1 menulis R1, kemudian I2 juga menulis ke R1\n",
        "\n",
        "I1 = \"R1 = 10\"       # Instruksi pertama menulis ke R1\n",
        "I2 = \"R1 = R2 + 5\"   # Instruksi kedua menulis ke R1\n",
        "\n",
        "# Simulasi nilai\n",
        "R2 = 50\n",
        "R1 = 0\n",
        "\n",
        "R1 = 10       # I1 menulis nilai 10 ke R1\n",
        "R1 = R2 + 5   # I2 menulis nilai 55 ke R1\n",
        "\n",
        "print(\"WAW:\")\n",
        "print(\"R1 =\", R1)\n",
        "print(\"R2 =\", R2)"
      ],
      "metadata": {
        "id": "p6IQDTg88SXT",
        "outputId": "1505cfa1-1996-462a-891b-6c77a9edda19",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "WAW:\n",
            "R1 = 55\n",
            "R2 = 50\n"
          ]
        }
      ]
    }
  ]
}