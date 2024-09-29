{
 "cells": [
  {
   "cell_type": "code",
<<<<<<< HEAD
   "execution_count": 1,
   "id": "2be7bbe0",
=======
   "execution_count": null,
   "id": "5539379d-7ef9-4757-94c1-9c276eb9b443",
   "metadata": {},
   "outputs": [],
   "source": [
    "# pip install flask"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "79454e86-8d20-4c09-8589-243ea74ffc30",
>>>>>>> 02b5ee17604b57daeaf672097f2d19c1e0eccf0c
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
<<<<<<< HEAD
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
=======
      "Requirement already satisfied: Flask-CORS in c:\\python310\\lib\\site-packages (4.0.1)\n",
      "Requirement already satisfied: Flask>=0.9 in c:\\python310\\lib\\site-packages (from Flask-CORS) (3.0.3)\n",
      "Requirement already satisfied: Werkzeug>=3.0.0 in c:\\python310\\lib\\site-packages (from Flask>=0.9->Flask-CORS) (3.0.3)\n",
      "Requirement already satisfied: Jinja2>=3.1.2 in c:\\python310\\lib\\site-packages (from Flask>=0.9->Flask-CORS) (3.1.4)\n",
      "Requirement already satisfied: itsdangerous>=2.1.2 in c:\\python310\\lib\\site-packages (from Flask>=0.9->Flask-CORS) (2.2.0)\n",
      "Requirement already satisfied: click>=8.1.3 in c:\\python310\\lib\\site-packages (from Flask>=0.9->Flask-CORS) (8.1.7)\n",
      "Requirement already satisfied: blinker>=1.6.2 in c:\\python310\\lib\\site-packages (from Flask>=0.9->Flask-CORS) (1.8.2)\n",
      "Requirement already satisfied: colorama in c:\\python310\\lib\\site-packages (from click>=8.1.3->Flask>=0.9->Flask-CORS) (0.4.6)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in c:\\python310\\lib\\site-packages (from Jinja2>=3.1.2->Flask>=0.9->Flask-CORS) (2.1.5)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: Ignoring invalid distribution -rotobuf (c:\\python310\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -rotobuf (c:\\python310\\lib\\site-packages)\n",
      "\n",
      "[notice] A new release of pip is available: 24.1.2 -> 24.2\n",
      "[notice] To update, run: python.exe -m pip install --upgrade pip\n"
     ]
    }
   ],
   "source": [
    "pip install Flask-CORS"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "8131be0d-7bd2-40e4-bf6f-8f61e961032a",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "1251a046-37c3-43c3-a126-148878f965d2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<flask_cors.extension.CORS at 0x1853bfdac80>"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from flask_cors import CORS\n",
    "from flask import Flask, jsonify\n",
    "app = Flask(__name__)\n",
    "CORS(app)\n",
    "@app.route('/api/data')\n",
    "def get_data():\n",
    "    data = {\n",
    "        'title': 'Welcome to Angular-Python App',\n",
    "        'message': 'This is an example integration between Angular and Python!'\n",
    "    }\n",
    "    return jsonify(data)\n",
    "@app.route('/api/search')\n",
    "def search():\n",
    "    data = {\n",
    "        'title': 'search to Angular-Python App',\n",
    "        'message': 'This is an example integration between Angular and Python!'\n",
    "    }\n",
    "    return jsonify(data)\n",
    "if __name__ == '__main__':\n",
    "    app.run()"
>>>>>>> 02b5ee17604b57daeaf672097f2d19c1e0eccf0c
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
<<<<<<< HEAD
   "id": "f8aa5071",
=======
   "id": "fd4564a1-e3ab-40b0-b009-15dd12ef50dc",
   "metadata": {},
   "outputs": [],
   "source": [
    "# app = Flask(__name__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "dbdf648c-702a-46dd-af98-f6f033cd1080",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "f86cdb89-24ea-4ba1-a4da-a0cd163eb622",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "53ffe160-ee58-442b-882f-2f62755a3759",
>>>>>>> 02b5ee17604b57daeaf672097f2d19c1e0eccf0c
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
<<<<<<< HEAD
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
=======
      "127.0.0.1 - - [30/Jul/2024 16:46:16] \"GET /api/data HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [30/Jul/2024 16:46:16] \"GET /api/search HTTP/1.1\" 200 -\n"
     ]
    }
   ],
   "source": []
>>>>>>> 02b5ee17604b57daeaf672097f2d19c1e0eccf0c
  },
  {
   "cell_type": "code",
   "execution_count": null,
<<<<<<< HEAD
   "id": "42654a59",
=======
   "id": "c7d7b4a6-d30d-4a0f-86a2-80f78935b3ea",
>>>>>>> 02b5ee17604b57daeaf672097f2d19c1e0eccf0c
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
<<<<<<< HEAD
   "version": "3.11.3"
=======
   "version": "3.10.5"
>>>>>>> 02b5ee17604b57daeaf672097f2d19c1e0eccf0c
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
