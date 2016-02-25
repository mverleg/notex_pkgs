
/* http://stackoverflow.com/a/23003221/723090 */
/* todo: add self-contained version (inline json) */
/* todo: add option to define mpld3-plugin-javascript */
/* todo: add resizing, fonts and other customizations, if they can/should be done client-side:
	http://stackoverflow.com/questions/16265123/resize-svg-when-window-is-resized-in-d3-js */
$('.mpld3-figure').each(function(k, elem) {
	if (elem.getAttribute('id')) {
		var fig_id = elem.getAttribute('id');
	} else {
		var fig_id = 'mpld3_' + Math.random().toString(36).slice(-8);
		elem.id = fig_id;
	}
	var json_src = elem.getAttribute('data-src');
	$.getJSON(json_src, function(fig_id, json) {
		mpld3.draw_figure(fig_id, json);
	}.bind(null, fig_id));
});


