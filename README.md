# chess

This micro-repo comprises little more than [one little script](https://github.com/microprediction/chess/blob/main/set.py), but that's all it
takes to use the general purpose prediction [api](http://api.microprediction.org/) and forecast bullet and blitz chess ratings for top players:

| Player            | Home                                                              | Blitz                                                                                                   |
|-------------------|-------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Hikaru Nakamura   | [Hikaru](https://www.chess.com/member/hikaru)                     | [on change](https://www.microprediction.org/stream_dashboard.html?stream=chess_blitz_level_Hikaru),  [daily](https://www.microprediction.org/stream_dashboard.html?stream=chess_blitz_daily_Hikaru)            |
| Daniel Naroditsky | [DanielNaroditsky](https://www.chess.com/member/danielnaroditsky) | [on change](https://www.microprediction.org/stream_dashboard.html?stream=chess_bullet_level_DanielNaroditsky), [daily](https://www.microprediction.org/stream_dashboard.html?stream=chess_bullet_daily_DanielNaroditsky) |
| Alireza Firouzja  | [Firouzja2003](https://www.chess.com/member/firouzja2003)         | [on change](https://www.microprediction.org/stream_dashboard.html?stream=chess_bullet_level_Firouzja2003), [daily](https://www.microprediction.org/stream_dashboard.html?stream=chess_bullet_daily_Firouzja2003)     |

... and some not-so-top players. We're more than happy to include your rating(s) too. Make a pull request modifying [config.py](https://github.com/microprediction/chess/blob/main/config.py), or just leave an issue with your chess.come username. Then look in [analysis](https://github.com/microprediction/chess/tree/main/analysis) some time later to see what is there. 

The script [set.py](https://github.com/microprediction/chess/blob/main/set.py) runs every hour, and creates a stream like [this one](https://www.microprediction.org/stream_dashboard.html?stream=chess_bullet_level_DanielNaroditsky). That stream is monitored by lots of time series algorithms who fight for supremacy. The result is distributional predictions that get slowly better over time and incorporate more exogenous data. For instance the algorithms have access to all public data including all games played. 

Oh yeah, and if you want to increase your bullet rating by 100 you can:
- Use right click to cancel pre-moves.
- Play the Halloween Gambit! See [The Halloween Gambit is Scarier Than Your Think](https://www.chess.com/blog/PinIsMightier/the-halloween-gambit-is-scarier-than-you-think-4).  

More soon at www.microprediction.com/blog about chess and the statistics of bullet opennings...

![](https://github.com/microprediction/chess/blob/main/bullet-chess-ai.png)
