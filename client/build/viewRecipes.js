class ViewRecipes{
    constructor(){}

    renderRecipes(recipes){
        for(let i=0; i<recipes.length; i++){
            let temp = ""
            for (let j=0; j< recipes[i]["ingredients"].length ; j++){
                temp += recipes[i]["ingredients"][j]
                temp += ' \n '
            }
            recipes["ingredients"] = temp
        }

        console.log(recipes["ingredients"])

        $("#recipes-container").empty()
        const source = $("#recipes-template").html()
        const templateRecipe = Handlebars.compile(source);
        $("#recipes-container").append(templateRecipe({recipes}))
    }

    // renderStatistic(statistics: Statistic[], statisticContainer: any){
    //     $(statisticContainer).empty()
    //     const source = $("#statistic-template").html()
    //     const templateStatistic = Handlebars.compile(source)
    //     $(statisticContainer).append(templateStatistic({statistics}))
    // }

    // removeStatistic(statisticContainer: any){
    //     $(statisticContainer).empty()
    // }
}