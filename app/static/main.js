$(document).ready(function() {
    window.ingredients = ["makers.","hackers.","engineers.","techies.", "learners."];

//    var debug = $("#debug");
    
    function flipText(newText) {
        flipUp == true ? ($("#new-text").text(newText), $("#old-text").hide("drop", {
            direction: "down"
        }, 300), $("#new-text").show("drop", {
            direction: "up"
        }, 300)) : ($("#old-text").text(newText), $("#old-text").show("drop", {
            direction: "up"
        }, 300), $("#new-text").hide("drop", {
            direction: "down"
        }, 300));
        flipUp = !flipUp; // Alternating flipping direction
    }

    var interval = 2e3; // 2 seconds
    var flipUp = true;
    var index = 0;
    var maxIndex = window.ingredients.length - 1;
    setInterval(function() {
        var nextText = window.ingredients[index];
//        debug.append("<p>"+window.ingredients[index]+"</p>");
        flipText(nextText);
        index = (index == maxIndex) ? 0 : index + 1;
     }, interval);
});