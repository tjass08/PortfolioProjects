<?php
/**
 * Plugin Name:       Cyber Risk Ranger: Spot the Phish
 * Description:       Serves the Spot the Phish challenge as a full-screen page at /spotthephish/.
 * Version:           1.1.0
 * Requires at least: 5.0
 * Requires PHP:      7.0
 * License:           GPL-2.0-or-later
 */

defined( 'ABSPATH' ) || exit;

/**
 * Site addresses (the part after the domain) and the game file each one opens.
 * Edit this list if the site already uses one of these addresses.
 */
function crr_games_addresses() {
	return array(
		'spotthephish'   => 'spot-the-phish.html',
		'spot-the-phish' => 'spot-the-phish.html',
	);
}

add_action( 'init', 'crr_games_serve', 1 );

function crr_games_serve() {
	$request = isset( $_SERVER['REQUEST_URI'] ) ? wp_unslash( $_SERVER['REQUEST_URI'] ) : ''; // phpcs:ignore WordPress.Security.ValidatedSanitizedInput.InputNotSanitized -- only compared against fixed addresses.
	$path    = (string) wp_parse_url( $request, PHP_URL_PATH );
	$base    = (string) wp_parse_url( home_url( '/' ), PHP_URL_PATH );
	if ( '' !== $base && 0 === strpos( $path, $base ) ) {
		$path = substr( $path, strlen( $base ) );
	}

	$games = crr_games_addresses();
	$slug  = strtolower( trim( $path, '/' ) );
	if ( ! isset( $games[ $slug ] ) ) {
		return;
	}

	$html = file_get_contents( __DIR__ . '/games/' . $games[ $slug ] ); // phpcs:ignore WordPress.WP.AlternativeFunctions.file_get_contents_file_get_contents
	if ( false === $html ) {
		return;
	}
	$html = str_replace( '__CRR_ASSETS__', esc_url( plugins_url( 'assets', __FILE__ ) ), $html );

	// Page-cache and optimization plugins rewrite inline scripts in ways that break the games,
	// so the page bypasses their output buffers.
	if ( ! defined( 'DONOTCACHEPAGE' ) ) {
		define( 'DONOTCACHEPAGE', true );
	}
	while ( ob_get_level() > 0 && ob_end_clean() ) {
		continue;
	}

	status_header( 200 );
	header( 'Content-Type: text/html; charset=utf-8' );
	header( 'X-Content-Type-Options: nosniff' );
	echo $html; // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped -- static page shipped with this plugin.
	exit;
}
