const moment = require('moment');

require('dotenv').config();
const { Client, IntentsBitField, ActivityType, GuildMembersChunk } = require('discord.js', 'moment.js');


const bot = new Client({
    intents: [
        IntentsBitField.Flags.Guilds,
        IntentsBitField.Flags.GuildMembers,
        IntentsBitField.Flags.GuildMessages,
        IntentsBitField.Flags.MessageContent,
    ],
});


bot.on('ready', (b) => {
    console.log(`O bot ${b.user.tag} ficou online! <3`);

    const guild = bot.guilds.cache.get(process.env.GUILD_ID);
     
    bot.user.setActivity({
        name: `O servidor ${guild.name} tem exatamente ${guild.memberCount} membros atualmente!`,
        type: ActivityType.Custom,
    });
});


bot.on('interactionCreate', (interaction)=>{

    if(!interaction.isChatInputCommand())
        return;

    if(interaction.commandName === "hello"){

        interaction.reply("Olá cachorrona");
    }

    if(interaction.commandName === "fuck"){

        interaction.reply("Vai se fuder puta inutil");
    }
    
    if(interaction.commandName === "oi"){
        
        const d = new Date();
        

        interaction.reply(`${moment(d).format('DD/MM/YYYY, h:mm:ss a')}`);
    }


});
 










bot.login(process.env.TOKEN);