# MUSIC RECS

[![](https://img.shields.io/badge/Made_with-Python3-blue?style=for-the-badge&logo=python)](https://www.python.org)
[![](https://img.shields.io/badge/IDE-VSCode-brightgreen?style=for-the-badge&logo=visual-studio-code)](https://code.visualstudio.com/)

A desktop application that analyses songs you like to build new playlists for you!

## Description:
This recommender system works by leveraging the _item similarity_ based _collaborative filtering_ model. 

You can use it to find **popular** or **similar** songs based as per your preference :)

## How it works:
Item-item filtering approach involves defining a co-occurrence matrix based on a song a user likes. We are seeking to answer a question: for each song, what number of times a user, who has listened to that song, will also listen to another set of other songs? 

Considering what you liked in the past, what other similar song that you will like based on what other similar user have liked?

## Features:
1. Popularity based recommendation: You can get any number of popular songs, i.e. those songs who have been played the most times by the highest number of unique users.
2. Item similarity based recommendation: You can input any number of songs you like with their title and artist. The system constructs a cooccurance matrix with this list to get you unique recommendations from other users who have also listened to these songs.

## Tech Stack:
1. Interface: GUI built using Tkinter library.
2. Preprocessing: Done using pandas and numpy libraries to clean and prepare the dataset.
3. Prediction: Scikit-learn library used for splitting the training set and evaluation metrics.

## Screenshots:
<img src="https://github.com/rubyruins/music-recs/blob/master/screenshots/music_interface.PNG" height="300">    <img src="https://github.com/rubyruins/music-recs/blob/master/screenshots/popular.PNG" height="300">    <img src="https://github.com/rubyruins/music-recs/blob/master/screenshots/similar.PNG" height="300">

## Dataset used | [The Million Song Dataset:](http://millionsongdataset.com/)
The Million Song Dataset is a freely-available collection of audio features and metadata for a million contemporary popular music tracks.

#### This is a desktop application built for our Python Programming project.

Made with 💖 by [Soumya Parekh](https://github.com/rubyruins), [Kanksha Pandey](https://github.com/KankshaP) and [Ankita Shelke](https://github.com/as959).
