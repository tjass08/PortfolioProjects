=== Cyber Risk Ranger: Spot the Phish ===
Requires at least: 5.0
Requires PHP: 7.0
Stable tag: 1.1.0
License: GPLv2 or later

Puts the Spot the Phish challenge from the Cyber Risk Ranger newsletter on the site as a full-screen page.

== Description ==

Once the plugin is active, the game opens at /spotthephish/ on the site (/spot-the-phish/ works too).

The game fills the whole screen, exactly like the standalone file. The plugin adds no settings, stores nothing in the database and collects nothing from visitors. Deactivating it takes the page down.

== Installation ==

1. In WordPress, go to Plugins > Add New Plugin > Upload Plugin.
2. Choose cyber-risk-ranger-games.zip and click Install Now.
3. Click Activate Plugin.
4. Open /spotthephish/ on the site and answer a question.

== Frequently Asked Questions ==

= An earlier version is already installed =

Upload this zip the same way and click "Replace current with uploaded". Version 1.0.0 also served the Defender Style quiz at /defenderstyle/; this version removes that page.

= Can I change the address? =

Yes. Edit the list in crr_games_addresses() in cyber-risk-ranger-games.php.

= The address shows a server "not found" page instead of the game =

The site is probably set to Plain permalinks. Any other choice under Settings > Permalinks fixes it.

= The game loads, but its buttons do nothing =

If the site sends a Content-Security-Policy header, the page needs script-src 'unsafe-inline' 'unsafe-eval', style-src 'unsafe-inline', img-src 'self' and font-src data:. CDN features that rewrite scripts, such as Cloudflare Rocket Loader, should be turned off for this address.

== Changelog ==

= 1.1.0 =
* Serves only Spot the Phish. The Defender Style quiz page is removed.

= 1.0.0 =
* First version, serving Spot the Phish and the Defender Style quiz.
