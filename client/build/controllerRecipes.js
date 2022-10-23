const modelRecipes = new ModelRecipes()
const viewRecipes = new ViewRecipes()

$("#get-recipes-button").on("click", async function(){
    const ingredient = $('#ingredient-name').val();
    const isGlutenFree = ($('#gluten-free').is(":checked")) ? true : false;
    const isDairyFree = ($('#dairy-free').is(":checked")) ? true : false;

    modelRecipes.featchRecipes(ingredient, isGlutenFree, isDairyFree).then(()=>{
        console.log(modelRecipes.recipes)
        viewRecipes.renderRecipes(modelRecipes.recipes)
    })
})