{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "JSON.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyPgJp8XHUwNxJ3aUCmKvF7f",
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
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
        "<a href=\"https://colab.research.google.com/github/vifirsanova/ASD-QA/blob/main/count_dataset_stats.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import json\n",
        "from pathlib import Path\n",
        "\n",
        "import statistics\n",
        "\n",
        "path_orig, path_short = Path('original.json'), Path('short.json')\n",
        "data_orig, data_short = json.loads(path_orig.read_text(encoding='utf-8')), json.loads(path_short.read_text(encoding='utf-8'))\n",
        "\n",
        "orig_q = []\n",
        "orig_a = []\n",
        "short_q = []\n",
        "short_a = []\n",
        "\n",
        "def listing(data, list_q, list_a):\n",
        "\n",
        "  for item in data['data']:\n",
        "    for paragraph in item['paragraphs']:\n",
        "      for qa in paragraph['qas']:\n",
        "        list_q.append(qa['question'])\n",
        "        list_a.append(qa['answers'][0]['text'])\n",
        "  \n",
        "  return list_q, list_a\n",
        "\n",
        "orig_q, orig_a  = listing(data_orig, orig_q, orig_a)\n",
        "short_q, short_a = listing(data_short, short_q, short_a)\n",
        "\n",
        "def avg_symbols(strings):\n",
        "  return round(sum(map(len, strings)) / len(strings))\n",
        "\n",
        "def avg_tokens(strings):\n",
        "  return round(statistics.mean([len(token) for token in [element.split() for element in strings]]))\n",
        "\n",
        "print('Average number of symbols in answers')\n",
        "print('Original dataset version', avg_symbols(orig_a))\n",
        "print('Shortened dataset version', avg_symbols(short_a))\n",
        "\n",
        "print('\\nAverage number of tokens in answers')\n",
        "print('Original dataset version', avg_tokens(orig_a))\n",
        "print('Shortened dataset version', avg_tokens(short_a))"
      ],
      "metadata": {
        "id": "2qlAo2YAV5Uu"
      },
      "execution_count": 1,
      "outputs": []
    }
  ]
}