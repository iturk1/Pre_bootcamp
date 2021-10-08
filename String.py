{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "4adc0d0b-0907-41e7-8a28-1d691e13d62e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello World\n"
     ]
    }
   ],
   "source": [
    "# 1. TASK: print \"Hello World\"copy\n",
    "print(\"Hello World\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "d961ffac-8b72-4397-8631-93c2d11b4887",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello 42\n"
     ]
    }
   ],
   "source": [
    "# 3a. print \"Hello 42!\" with the number in a variable\n",
    "name = 42\n",
    "print(\"Hello\", name)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "0a2238a0-b5f5-4c6d-bee6-57b7ea3c9146",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "can only concatenate str (not \"int\") to str",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-42-aee14cde57dc>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;31m# 3b. print \"Hello 42!\" with the number in a variable\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[0mname\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;36m42\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 3\u001b[0;31m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Hello\"\u001b[0m \u001b[0;34m+\u001b[0m \u001b[0mname\u001b[0m \u001b[0;34m)\u001b[0m  \u001b[0;31m# with a +      -- this one should give us an error!\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m: can only concatenate str (not \"int\") to str"
     ]
    }
   ],
   "source": [
    "# 3b. print \"Hello 42!\" with the number in a variable\n",
    "name = 42\n",
    "print(\"Hello\" + name  )\t# with a +\t-- this one should give us an error!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "3f1cbc78-55ff-4e5b-a854-0def877d41b7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello Turki\n"
     ]
    }
   ],
   "source": [
    "# 2a. print \"Hello Noelle!\" with the name in a variable\n",
    "name = \"Turki\"\n",
    "print(\"Hello\", name)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "41ec9310-2fbb-462b-8289-8cb2f9377a0a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello Turki\n"
     ]
    }
   ],
   "source": [
    "# 2b. print \"Hello Noelle!\" with the name in a variable\n",
    "name = \"Turki\"\n",
    "print(\"Hello \" + name )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "dc379244-99ca-4459-b057-ee067661463f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "I love to eat sushi and pizza.\n",
      "I love to eat sushi and pizza.\n"
     ]
    }
   ],
   "source": [
    "# 4. print \"I love to eat sushi and pizza.\" with the foods in variables\n",
    "fave_food1 = \"sushi\"\n",
    "fave_food2 = \"pizza\"\n",
    "print(\"I love to eat {} and {}.\".format(fave_food1, fave_food2)) # with .format()\n",
    "print(f\"I love to eat {fave_food1} and {fave_food2}.\") # with an f string"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ab39b3c3-67c9-48e3-a236-e2c3f3cb08c6",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
