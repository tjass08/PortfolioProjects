=== Cyber Risk Ranger Games ===
Requires at least: 5.0
Requires PHP: 7.0
Stable tag: 1.0.0
License: GPLv2 or later

Puts the two Cyber Risk Ranger newsletter games on the site as full-screen pages.

== Description ==

Once the plugin is active, the games open at these addresses on the site:

* Spot the Phish: /spotthephish/ (also /spot-the-phish/)
* What's Your Defender Style?: /defenderstyle/ (also /defender-style/)

Each game fills the whole screen, exactly like the standalone files. The plugin adds no settings, stores nothing in the database and collects nothing from visitors. Deactivating it takes both pages down.

== Installation ==

1. In WordPress, go to Plugins > Add New Plugin > Upload Plugin.
2. Choose cyber-risk-ranger-games.zip and click Install Now.
3. Click Activate Plugin.
4. Open /spotthephish/ and /defenderstyle/ on the site and answer a question in each game.

== Frequently Asked Questions ==

= Can I change the addresses? =

Yes. Edit the list in crr_games_addresses() in cyber-risk-ranger-games.php.

= The address shows a server "not found" page instead of the game =

The site is probably set to Plain permalinks. Any other choice under Settings > Permalinks fixes it.

= The game loads, but its buttons do nothing =

If the site sends a Content-Security-Policy header, Spot the Phish needs script-src 'unsafe-inline' 'unsafe-eval', style-src 'unsafe-inline', img-src 'self' and font-src data:. The Defender Style quiz needs script-src 'unsafe-inline', style-src 'unsafe-inline' https://fonts.googleapis.com, font-src https://fonts.gstatic.com and img-src data: blob:. CDN features that rewrite scripts, such as Cloudflare Rocket Loader, should be turned off for these two addresses.
