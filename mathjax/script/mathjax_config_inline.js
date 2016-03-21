
MathJax.Hub.Config({
    extensions: ["tex2jax.js", "mml2jax.js", "TeX/AMSmath.js", "TeX/AMSsymbols.js"],
    jax: ["input/TeX", "input/MathML", "output/HTML-CSS", "output/NativeMML"],
    tex2jax: {
        inlineMath: [ ['$[',']$'] ],
        displayMath: [ ['$$[',']$$'] ],
        processEscapes: true
    },
    showProcessingMessages: false,
    messageStyle: "none",
    positionToHash: true,  /* todo: good idea? */
    mtextFontInherit: true,  /* todo: good idea? */
    "HTML-CSS": { availableFonts: ["TeX"] }
});


