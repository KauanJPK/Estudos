require('dotenv').config();
const{REST, Routes} = require('discord.js');

const commands = [

    {
        name: 'hello',
        description: 'Say hello back!',
    },

    {
        name: 'fuck',
        description: 'say fuck to the user',


    },

    {
        name: 'oi',
        description: 'mensagem para lucas',


    },

];
 
    const rest = new REST({ version: '10' }).setToken(process.env.TOKEN);

(async() => {

    try{

        console.log("Registrando comandos para o bot");

        await rest.put(

            Routes.applicationGuildCommands(

                process.env.CLIENT_ID,
                process.env.GUILD_ID
            ),

            { body: commands}

        );

        console.log("Comandos registrados com sucesso");

    } catch (error){
        console.log(`Houve um pequeno erro ${error}`);
    }

})();