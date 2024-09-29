{
<<<<<<< HEAD
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "796d4a9a-aab3-4d2f-864a-e2c93d447a52",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "ERROR: You must give at least one requirement to install (see \"pip help install\")\n",
      "\n",
      "[notice] A new release of pip is available: 24.0 -> 24.2\n",
      "[notice] To update, run: python.exe -m pip install --upgrade pip\n"
     ]
    }
   ],
   "source": [
    "pip install --upgrade"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "26274773-9f66-4cd3-9db9-27004627f7d2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: flask in c:\\users\\the user\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (3.0.3)\n",
      "Requirement already satisfied: Werkzeug>=3.0.0 in c:\\users\\the user\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from flask) (3.0.3)\n",
      "Requirement already satisfied: Jinja2>=3.1.2 in c:\\users\\the user\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from flask) (3.1.4)\n",
      "Requirement already satisfied: itsdangerous>=2.1.2 in c:\\users\\the user\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from flask) (2.2.0)\n",
      "Requirement already satisfied: click>=8.1.3 in c:\\users\\the user\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from flask) (8.1.7)\n",
      "Requirement already satisfied: blinker>=1.6.2 in c:\\users\\the user\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from flask) (1.8.2)\n",
      "Requirement already satisfied: colorama in c:\\users\\the user\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from click>=8.1.3->flask) (0.4.6)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in c:\\users\\the user\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from Jinja2>=3.1.2->flask) (2.1.5)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n",
      "[notice] A new release of pip is available: 24.0 -> 24.2\n",
      "[notice] To update, run: python.exe -m pip install --upgrade pip\n"
     ]
    }
   ],
   "source": [
    "pip install flask"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "edf5a7fd-ba0e-4335-bcf1-7ebe2900d34d",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask, jsonify"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "44e8477b-1a42-42f2-a155-c41983572d8d",
   "metadata": {
    "scrolled": true
   },
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
      "Press CTRL+C to quit\n"
     ]
    }
   ],
   "source": [
    "app = Flask(__name__)\n",
    "@app.route('/api/data')\n",
    "def get_data():\n",
    "    data = {\n",
    "        'title': 'Welcome to Angular-Python App',\n",
    "        'message': 'This is an example integration between Angular and Python!'\n",
    "    }\n",
    "    return jsonify(data)\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run()"
   ]
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
   "version": "3.12.4"
  }
 },
=======
 "cells": [],
 "metadata": {},
>>>>>>> 02b5ee17604b57daeaf672097f2d19c1e0eccf0c
 "nbformat": 4,
 "nbformat_minor": 5
}
