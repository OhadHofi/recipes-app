class ViewRecipes{
    constructor(){}

    renderRecipes(recipes){
        $("#recipes-container").empty()
        const source = $("#recipes-template").html()
        const templateRecipe = Handlebars.compile(source);
        $("#recipes-container").append(templateRecipe({recipes}))
    }

    pop(text){
        alert(text);
    }
}