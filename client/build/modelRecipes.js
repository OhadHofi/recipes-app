class ModelRecipes{
    recipes

    constructor(){
    }

    async featchRecipes(ingredient, isGlutenFree, isDairyFree){
        const url = `/recipes/${ingredient}?dairy=${isGlutenFree}&gluten=${isDairyFree}`
        await $.get(url).then((recipes) => {
            this.recipes = recipes
        })
    }
}