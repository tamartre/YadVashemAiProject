{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "2be7bbe0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Defaulting to user installation because normal site-packages is not writeable\n",
      "Requirement already satisfied: flask in c:\\programdata\\anaconda3\\lib\\site-packages (2.2.2)\n",
      "Requirement already satisfied: Werkzeug>=2.2.2 in c:\\programdata\\anaconda3\\lib\\site-packages (from flask) (2.2.3)\n",
      "Requirement already satisfied: Jinja2>=3.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from flask) (3.1.2)\n",
      "Requirement already satisfied: itsdangerous>=2.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from flask) (2.0.1)\n",
      "Requirement already satisfied: click>=8.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from flask) (8.0.4)\n",
      "Requirement already satisfied: colorama in c:\\programdata\\anaconda3\\lib\\site-packages (from click>=8.0->flask) (0.4.6)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from Jinja2>=3.0->flask) (2.1.1)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install flask"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f8aa5071",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app '__main__'\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\n",
      " * Running on http://127.0.0.1:5000\n",
      "Press CTRL+C to quit\n",
      "127.0.0.1 - - [28/Jul/2024 17:23:55] \"GET /api/data HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [28/Jul/2024 17:23:55] \"GET /api/search HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [28/Jul/2024 17:23:55] \"GET /api/search HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [28/Jul/2024 17:23:55] \"GET /api/data HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [28/Jul/2024 17:23:55] \"GET /api/data HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [28/Jul/2024 17:23:55] \"GET /api/search HTTP/1.1\" 200 -\n"
     ]
    }
   ],
   "source": [
    "from flask import Flask, jsonify\n",
    "app = Flask(__name__)\n",
    "\n",
    "\n",
    "@app.route('/api/data')\n",
    "def get_data():\n",
    "    data = {\n",
    "        'title': 'practicom',\n",
    "        'message': 'the smart workers!'\n",
    "    }\n",
    "    return jsonify(data)\n",
    "\n",
    "@app.route('/api/search')\n",
    "def search():\n",
    "    data = {\n",
    "        'words':'positions'\n",
    "    }\n",
    "    return jsonify(data)\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "42654a59",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
