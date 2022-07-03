# Tic-Tac-Toe

**Tic-Tac-Toe Game** is a two-player game. Each player takes turns marking the spaces in a three-by-three grid with X or O. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row is the winner.

Time spent: **2** hours spent in total

## Feature of the Game

The following functionality is completed:

- [x] Two Users can play this game at a time.
- [x]	Users will be asked to input the position where they want their mark at on the board.
- [x] After each turn, both Users can see the updated board with X's and O's.
- [x] If player X or player O manage to place three of their marks in horizontal, vertical or diagonal manner then a message will be printed to the screen, displaying the winner.
- [x] In case of the tie between two players, a "Match Over" message will be printed to the screen.


## Video Walkthrough


![Tic Tac Toe](https://user-images.githubusercontent.com/89542741/177040239-a2271dca-e18f-4a35-80e4-4fb688680873.gif)


## Notes

Describe any challenges encountered while building this game ?

I encountered a challenge while building this game. I had made a 2D array named "wins" to check all possibilities in which a user can win a game. In this array, initially, I forgot to add the the diagonal possibility. Therefore, when I ran the program, my X user had got three marks in a diagonal manner but my program was unable to detect the win of my X user. When I saw this bug, I knew the issue had to be in my "checkWin" method. Hence, once I added all possible win cases to my 2D array, then this error went away and my program ran fine.

## Open-source libraries used

- [Android Async HTTP](https://github.com/codepath/CPAsyncHttpClient) - Simple asynchronous HTTP requests with JSON parsing
- [Glide](https://github.com/bumptech/glide) - Image loading and caching library for Android

## License

    Copyright [2022] [Kashaf Mujeeb]

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

https://www.youtube.com/watch?v=2ZDnw6ifdSI
