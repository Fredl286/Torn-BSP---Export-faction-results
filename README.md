# Torn BSP - Faction Export to CSV Tool

This simple Python tool uses [TDup's](https://www.torn.com/profiles.php?XID=2660552) Battle stat prediction backend to predict stats for all users in a specified faction, and export the results to a csv file.

You will need access with a valid API key for the plugin:
[BSP Forum Thread](https://www.torn.com/forums.php#/p=threads&f=67&t=16290324)

## Usage policy
I am including [TDup's](https://www.torn.com/profiles.php?XID=2660552) usage policy here as this applies to the usage of this script:

 - Don't spam requests (don't ddos the service)
 - Don't take my customers away from me by "stealing" the data.
##  Usage
This tool is simple to use, you will simply need to input your valid API key for BSP, and an API key that has public access to grab a list of users in the faction you want.

These should be input into 'example.env' which should be renamed to just '.env' before running the script.

#### Python Libraries required
 - requests
 - python-dotenv

Once ready, run main.py and you will be prompted to input a faction ID, which can be easily located from the URL when looking at a faction in Torn:

    https://www.torn.com/factions.php?step=profile&ID=50170#/

The results will output the following values to output.csv for use in your own war reporting.

 - `id`
 - `name`
 - `level`
 - `TBS`
 - `Score`
 - `PredictionDate`

##  Contact
If anyone has any questions about my short script, feel free to contact me via [Torn](https://www.torn.com/profiles.php?XID=3392714) or Discord **fred6564**