{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9cb18c50-c1ee-4556-b132-0ad79236a88c",
   "metadata": {},
   "outputs": [],
   "source": [
    "# pip install Flask-CORS"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e45a9cc0-006a-490b-9ede-5822590f6fe2",
   "metadata": {},
   "outputs": [],
   "source": [
    "# pip install flask"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "eb2b302b-c466-4791-a37b-bf5f99a00ec1",
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import json\n",
    "\n",
    "def generate_tree(path):\n",
    "    tree = {}\n",
    "    tree['name'] = os.path.basename(path)\n",
    "    tree['type'] = 'folder' if os.path.isdir(path) else 'file'\n",
    "    if os.path.isdir(path):\n",
    "        tree['children'] = [generate_tree(os.path.join(path, item)) for item in os.listdir(path)]\n",
    "    return tree\n",
    "\n",
    "data_path = 'data'  # צייני את הנתיב לתיקיית המידע שלך כאן\n",
    "tree = generate_tree(data_path)\n",
    "print(json.dumps(tree, indent=4))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "57b5c448-440f-4ca9-93cc-a2e61a8c9e7e",
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "from flask import Flask, jsonify\n",
    "from flask_cors import CORS\n",
    "app = Flask(__name__)\n",
    "CORS(app)\n",
    "@app.route('/api/data')\n",
    "def get_data():\n",
    "    data = {\n",
    "        'title': 'Welcome to Angular-Python App',\n",
    "        'message': 'This is an example integration between Angular and Python!'\n",
    "    }\n",
    "    return jsonify(data)\n",
    "# if __name__ == '__main__':\n",
    "#     app.run()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e602bc51-41d6-4b6a-9ad6-3d1786a78a65",
   "metadata": {},
   "outputs": [],
   "source": [
    "# import os\n",
    "# from flask import Flask, jsonify, Response\n",
    "# from flask_cors import CORS\n",
    "# import json\n",
    "\n",
    "# app = Flask(__name__)\n",
    "# CORS(app)\n",
    "\n",
    "# # Function to generate a tree structure of folders and files\n",
    "# def generate_tree(path):\n",
    "#     tree = {}\n",
    "#     tree['name'] = os.path.basename(path)\n",
    "#     tree['type'] = 'folder' if os.path.isdir(path) else 'file'\n",
    "#     if os.path.isdir(path):\n",
    "#         tree['children'] = [generate_tree(os.path.join(path, item)) for item in os.listdir(path)]\n",
    "#     return tree\n",
    "\n",
    "# @app.route('/api/tree', methods=['GET'])  # Ensure to specify methods for the route\n",
    "# def get_tree():\n",
    "#     data_path = 'data'  # Specify the path to your data folder\n",
    "#     tree = generate_tree(data_path)\n",
    "#     response = Response(response=json.dumps(tree, indent=4), status=200, content_type='application/json')\n",
    "#     return response\n",
    "\n",
    "# if __name__ == '__main__':\n",
    "#     app.run()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b4a9db45-fbb8-43e8-a5df-84c4193c3d15",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask\n",
    "app = Flask(__name__)\n",
    "\n",
    "@app.route(\"/\")\n",
    "def hello():\n",
    "    return \"Hello World!\"\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d4502524-6541-4d1e-9761-a07b07118a0e",
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
      "Press CTRL+C to quit\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "from flask import Flask, jsonify, Response\n",
    "from flask_cors import CORS\n",
    "import json\n",
    "\n",
    "app = Flask(__name__)\n",
    "CORS(app)\n",
    "\n",
    "\n",
    "@app.route('/api/data')\n",
    "def get_data():\n",
    "    data = {\n",
    "        'title': 'Welcome to Angular-Python App',\n",
    "        'message': 'This is an example integration between Angular and Python!'\n",
    "    }\n",
    "    return jsonify(data)\n",
    "\n",
    "\n",
    "def generate_tree(path):\n",
    "    tree = {}\n",
    "    tree['name'] = os.path.basename(path)\n",
    "    tree['type'] = 'folder' if os.path.isdir(path) else 'file'\n",
    "    if os.path.isdir(path):\n",
    "        tree['children'] = [generate_tree(os.path.join(path, item)) for item in os.listdir(path)]\n",
    "        return tree\n",
    "\n",
    "@app.route('/api/tree')\n",
    "def get_tree():\n",
    "    data_path = 'data'  # Specify the path to your data folder\n",
    "    try:\n",
    "        tree = generate_tree(data_path)\n",
    "        response = Response(response=json.dumps(tree, indent=4))\n",
    "        return response\n",
    "    except Exception as e:\n",
    "        error_message = {'error': str(e)}\n",
    "        response = Response(response=json.dumps(error_message), status=500, content_type='application/json')\n",
    "        return response\n",
    "\n",
    "\n",
    "@app.route(\"/api/hello\")\n",
    "def hello():\n",
    "    return \"Hello World!\"\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a21b65bd-4dd3-45cd-9b8e-a49cf0f1234b",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask_cors import CORS\n",
    "cors = CORS(app)"
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
 "nbformat": 4,
 "nbformat_minor": 5
}
