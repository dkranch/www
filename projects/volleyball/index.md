I have a few tools I've made for coaching. Each is described below, with links to the tools.

The list of tools is:
- <a href="#sr">Service Receive Tracking</a>
- <a href="#season">Season Serve Receive Tracking</a>
- <a href="#matchstat">Match Stat Tracking</a>
- <a href="#matchsummary">Match Summary</a>

## Serve Receive Tracking
<a name="sr">I have a tool</a> for tracking performance during serve receive. When we set up a drill, we quickly rate players passes and give them feedback after the drill. This duplicates a paper/pencil process, but provides calculations immediately.

I have this as a simple 1 page web-based tool. I can download and run this from a tablet easily. If you want to use it, you need a place to download from as many systems don't allow a file to be opened and work. I click the links below on my iPad and then I can click the numbers to rate a player's pass. If I mess up, I click undo and remove the last click. This gives me immediate passing feedback.

- <a href="14black.html" target="_blank">14 Black</a>
- <a href="17red.html" target="_blank">17 Red</a>

I save off the data in JSON, which I can then copy to a spreadsheet for season long analysis. You can click to edit player's names, which are saved on that device. Change the date and time to change the download file. Click "Reset stats" to set things to 0.

If you host this on your own server, you can edit the JSON to pre-load player names. Line 450 is where you change names.

## Season Analysis
<a name="season">I created a tool</a> for analyzing season-long serve receive performance. Actually, I didn't, but Claude did. In this case, I take the csv exports from the tool above and produce a sample report. You can see a sample (with made up data, don't tell my players this is their performance) here: <a href="14blacksample.html" target="_blank">14 Black Sample</a>

The way to do this is put all the csvs in a folder. You then download <a href="SRStatAnalyzer.zip">this zip file</a> and extract is to the same place as the csvs. You need Python 3.6 or newer. 

Then run: python analyze.py . 14black.html

The dot (.) is the current folder and the 14black.html is the output file that will be generated with the analysis results. Open that to see your results.

## Match Stats
<a name="matchstat">Tracking stats</a> during a match is something that needs to be quick and easy. This is more of a trend capture than a record of what happened. So many tools make this hard, and try to be exacting. I just want stats that 
1 - help me validate coaches impressions
2 - gives kids a view of their performance

I do this on paper during the match and then transfer the data to a spreadsheet afterward for analysis. That's a pain. I made a quick tool that essentially duplicates paper.

- <a href="matchstats.html" target="_blank">Match Stats Tool</a>
- <a href="matchstats14b.html" target="_blank">14 Black Stats</a>
- <a href="matchstats17r.html" target="_blank">17 Red Stats</a>

A few notes:
- Enter the event, opponent, set, and change date/time
- Player names are preloaded here for my teams. To do yours, just change the names. Line 71 has players
- Click a stat to record it. Click undo to remove the last entry
- Manually click scores to add them
- export to save. Uses the event and date/time to create the filename

## Match Summary
<a name="matchsummary">Summary tool</a> that loads 1 or more exports from the stats above and gives you totals by player for quick analysis.

- <a href="matchsummary.html" target="_blank">Match Summary Tool</a>

Click load and select the export files.