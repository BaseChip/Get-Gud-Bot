import discord
import asyncio
import KEYS
import os
import sqlite3
import random
import string

conn = sqlite3.connect("database.db")
cur = conn.cursor()



async def nachricht(message, channel):
    chan = client.get_channel(channel)
    await chan.send(content=message)


async def sendmsg(message, channel, dtime):
    chan = client.get_channel(channel)
    nach = await chan.send(content=str(message))
    await asyncio.sleep(int(dtime))
    try:
        await nach.delete()
        return True
    except discord.errors.Forbidden:
        print("Verboten! Nachricht: %s\nChannel: %s" % (str(message), chan.name))
        pass
    except discord.errors.HTTPException:
        pass
    except:
        return False

async def ev(title, des, days, houres, minutes, reward):
    try:
        print("ev1")
        cou = 0
        d = int(days)
        h = int(houres)
        m = int(minutes)
        while d > 0:
            cou = cou + 86400
            d = d -1
            print("ev2")
        while h > 0:
            cou = cou + 3600
            h = h -1
            print("ev3")
        while m > 0:
            cou = cou + 60
            m = m-1
            print("ev4")
        print(cou)
        await nachricht("A new event %s has been created in %s days and %sh:%sm @here" % (title, days, houres, minutes), 411821497578029056)
        await asyncio.sleep(cou)
        chan = client.get_channel(415845094521044992)
        await chan.send(content="The event %s is over please announce a winner with gg.winner" % (title))
        '''
        finished = False
        global evtitle
        evtitle = title
        global evdes
        evdes = des
        global evd
        global evh
        global evm
        evh = houres
        evd = days
        d = days
        h = houres
        m = minutes
        n = 0
        await nachricht("A new event %s has been created in %s days and %sh:%sm" % (title, days, houres, minutes), 411821497578029056)
        while finished == False:
            if m != 0:
                m = m - 1
                global evm
                evm = m
                await asyncio.sleep(60)
            elif m == 0:
                if h != 0:
                    h = h - 1
                    m = 60
                    global evm
                    evm = m
                    global evh
                    evh = h
                elif h == 0:
                    if d != 0:
                        d = d - 1
                        h = 23
                        m = 60
                        global evd
                        global evh
                        global evm
                        evm = m
                        evh = h
                        evd = d
                    elif d == 0:
                        # a channel to announce
                        evtitle = "NO"
                        evdes = "NO"
                        finished = True
                        getguid = await client.get_guild(392983553912209409)
                        win = random.randint(0, len(getguid.members))
                        counter = 0
                        for memb in getguid.members:
                            if counter==win:
                                global winner
                                winner = [memb.mention, memb.name, memb.id]
                                await nachricht("Hey %s you have won the event %s" % (winner[0], title), 411821497578029056)
                            counter += 1 '''


    except Exception as e:
        print(e)
        return False


async def autev1(title, des, days, houres, minutes, reward):
    try:
        finished = False
        global autev1name
        autev1name = title
        global autev1des
        autev1des = des
        d = days
        h = houres
        m = minutes
        n = 0
        while finished == False:
            if m != 0:
                m = m - 1
                await asyncio.sleep(60)
            elif m == 0:
                if h != 0:
                    h = h - 1
                    m = 60
                elif h == 0:
                    if d != 0:
                        d = d - 1
                        h = 23
                        m = 60
                    elif d == 0:
                        # a channel to announce
                        d = days
                        h = houres
                        m = minutes
    except:
        return False


async def autev2(title, des, days, houres, minutes, reward):
    try:
        finished = False
        global autev2name
        autev2name = title
        global autev2des
        autev2des = des
        d = days
        h = houres
        m = minutes
        n = 0
        while finished == False:
            if m != 0:
                m = m - 1
                if m == 30 and d == 0 and h == 0:
                    await nachricht("Autoevent ends in 30 minutes")
                await asyncio.sleep(60)
            elif m == 0:
                if h != 0:
                    h = h - 1
                    m = 60
                elif h == 0:
                    if d != 0:
                        d = d - 1
                        h = 23
                        m = 60
                    elif d == 0:
                        # a channel to announce
                        d = days
                        h = houres
                        m = minutes
    except:
        return False


class MyClient(discord.Client):
    async def on_ready(self):
        cur.execute("CREATE TABLE IF NOT EXISTS tokens (userid INTEGER, ggtokens INTEGER)")
        cur.execute("CREATE TABLE IF NOT EXISTS ggevent (reward INTEGER)")
        cur.execute("CREATE TABLE IF NOT EXISTS ggking (role INTEGER, rrole INTEGER)")
        cur.execute("CREATE TABLE IF NOT EXISTS revent (name TEXT, description TEXT, reward INTEGER)")
        cur.execute("CREATE TABLE IF NOT EXISTS vote (channelid INTEGER)")
        cur.execute("CREATE TABLE IF NOT EXISTS store1 (preis INTEGER)")
        cur.execute("CREATE TABLE IF NOT EXISTS store2 (preis INTEGER)")
        cur.execute("CREATE TABLE IF NOT EXISTS store3 (preis INTEGER)")
        cur.execute("CREATE TABLE IF NOT EXISTS store4 (preis INTEGER)")
        cur.execute("CREATE TABLE IF NOT EXISTS store5 (preis INTEGER)")
        cur.execute("CREATE TABLE IF NOT EXISTS voting (canvote INTEGER, hasvoted INTEGER)")
        print("Bot is ready\n===")

    async def on_message(self, message):
        if message.content.startswith("gg."):
            invoke = message.content[3:].split(" ")[0]
            args = message.content.split(" ")[1:]

            if invoke == "ping":
                await sendmsg("Pong", message.channel.id, 5)

            if invoke == "tokens":
                cur.execute("SELECT * FROM tokens WHERE userid=?", (message.author.id,))
                iex = cur.fetchall()
                if str(iex) != "[]":
                    cur.execute("SELECT ggtokens FROM tokens WHERE userid=?", (message.author.id,))
                    tokens = cur.fetchone()[0]
                    msg = "You have %s GG Tokens that can be used in the store by using the command gg.store" % (
                        str(tokens))
                    chan = message.channel.id
                    await sendmsg(msg, chan, 10)
                else:
                    chan = message.channel.id
                    await sendmsg("Sorry you have no GG Tokens!", chan, 20)

            if invoke == "setup" and message.guild.owner_id == message.author.id:
                com = (message.content).replace("gg.setup", "")
                print(com)

                def c(m):
                    if m.author.id == message.author.id and m.channel.id == message.channel.id:
                        return m

                if com.startswith(" store"):
                    chan = message.channel.id
                    await nachricht("Which entry do you want to edit/create (1-5)", chan)
                    enter = await client.wait_for("message", check=c, timeout=None)
                    entery = enter.content
                    if entery=="1":
                        await message.channel.send(content="Please send me now the ggtoken amount")
                        amm = await client.wait_for("message", check=c, timeout=None)
                        cur.execute("SELECT preis FROM store1")
                        ex = cur.fetchall()
                        if str(ex) != "[]":
                            cur.execute("UPDATE store1 SET preis=?", (int(amm),))
                        else:
                            cur.execute("INSERT INTO store1 (preis) VALUES(?)", (int(amm),))
                    elif entery=="2":
                        await message.channel.send(content="Please send me now the ggtoken amount")
                        amm = await client.wait_for("message", check=c, timeout=None)
                        cur.execute("SELECT preis FROM store2")
                        ex = cur.fetchall()
                        if str(ex) != "[]":
                            cur.execute("UPDATE store2 SET preis=?", (int(amm),))
                        else:
                            cur.execute("INSERT INTO store2 (preis) VALUES(?)", (int(amm),))
                    elif entery=="3":
                        await message.channel.send(content="Please send me now the ggtoken amount")
                        amm = await client.wait_for("message", check=c, timeout=None)
                        cur.execute("SELECT preis FROM store3")
                        ex = cur.fetchall()
                        if str(ex) != "[]":
                            cur.execute("UPDATE store3 SET preis=?", (int(amm),))
                        else:
                            cur.execute("INSERT INTO store3 (preis) VALUES(?)", (int(amm),))
                    elif entery=="4":
                        await message.channel.send(content="Please send me now the ggtoken amount")
                        amm = await client.wait_for("message", check=c, timeout=None)
                        cur.execute("SELECT preis FROM store2")
                        ex = cur.fetchall()
                        if str(ex) != "[]":
                            cur.execute("UPDATE store4 SET preis=?", (int(amm),))
                        else:
                            cur.execute("INSERT INTO store4 (preis) VALUES(?)", (int(amm),))
                    elif entery=="5":
                        await message.channel.send(content="Please send me now the ggtoken amount")
                        amm = await client.wait_for("message", check=c, timeout=None)
                        cur.execute("SELECT preis FROM store5")
                        ex = cur.fetchall()
                        if str(ex) != "[]":
                            cur.execute("UPDATE store5 SET preis=?", (int(amm),))
                        else:
                            cur.execute("INSERT INTO store5 (preis) VALUES(?)", (int(amm),))

                if com.startswith(" vote"):
                    try:
                        chan = message.channel.id
                        await nachricht("Please send me the channel id where i should send the votes", chan)
                        ci = await client.wait_for("message", check=c, timeout=None)
                        cid = int(ci.content)
                        cur.execute("SELECT * FROM vote")
                        ex = cur.fetchall()
                        if str(ex) != "[]":
                            cur.execute("UPDATE vote SET channelid=?", (cid,))
                            conn.commit()
                        else:
                            cur.execute("INSERT INTO vote VALUES (?)", (cid,))
                            conn.commit()
                        await nachricht("Successful!", chan)
                    except Exception as e:
                            await nachricht("Error: "+e, chan)
                if com.startswith(" king"):
                    chan = message.channel.id
                    await nachricht("Please send me now the role id", chan)
                    w = await client.wait_for("message", check=c, timeout=None)
                    cur.execute("SELECT role FROM ggking")
                    ie = cur.fetchall()
                    if str(ie) == "[]":
                        try:
                            cur.execute("INSERT INTO ggking (role) VALUES (?)", (int(w.content),))
                            conn.commit()
                            await nachricht("Success, gg.king Role has been set!", chan)
                        except:
                            await nachricht("Unsuccessful, gg.king Role has not been set!", chan)
                    else:
                        try:
                            cur.execute("UPDATE ggking SET role=?", (int(w.content),))
                            conn.commit()
                            await nachricht("Success, gg.king Role has been set!", chan)
                        except:
                            await nachricht("Unsuccessful, gg.king Role has not been set!", chan)

                if com.startswith(" revent"):
                    try:
                        chan = message.channel.id
                        await nachricht("Plase send me now the event name?", chan)
                        w1 = await client.wait_for("message", check=c, timeout=None)
                        name = str(w1.content)
                        await nachricht("Please send me now the event description", chan)
                        w2 = await client.wait_for("message", check=c, timeout=None)
                        desc = str(w2.content)
                        await nachricht("Please send me now the reward", chan)
                        w3 = await client.wait_for("message", check=c, timeout=None)
                        reward = str(w3.content)
                        cur.execute("SELECT * FROM revent")
                        ex = cur.fetchall()
                        if str(ex) == "[]":
                            cur.execute("INSERT INTO revent(name, description, reward) VALUES (?, ?, ?)", (name, desc, reward))
                            conn.commit()
                            await nachricht("gg.revent setup Successful!", chan)
                        else:
                            cur.execute("UPDATE revent SET name=?, description=?, reward=?", (name, desc, reward))
                            conn.commit()
                            await nachricht("gg.revent setup Successful!", chan)
                    except:
                        await nachricht("gg.revent setup incorrect, please try again", chan)

                if com.startswith(" rking"):
                    chan = message.channel.id
                    await nachricht("Please send me now the role id", chan)
                    w = await client.wait_for("message", check=c, timeout=None)
                    cur.execute("SELECT rrole FROM ggking")
                    ie = cur.fetchall()
                    if str(ie) == "[]":
                        try:
                            cur.execute("INSERT INTO ggking (rrole) VALUES (?)", (int(w.content),))
                            conn.commit()
                            await nachricht("Success, gg.rking Role has been set!", chan)
                        except:
                            await nachricht("Unsuccessful, gg.rking Role has not been set!", chan)
                    else:
                        try:
                            cur.execute("UPDATE ggking SET rrole=?", (int(w.content),))
                            conn.commit()
                            await nachricht("Success, gg.rking Role has been set!", chan)
                        except:
                            await nachricht("Unsuccessful, gg.rking Role has not been set!", chan)

                if com.startswith(" event newevent"):
                    chan = message.channel.id
                    await nachricht("Please send me now the reward for the event command", chan)
                    wf = await client.wait_for("message", check=c, timeout=None)
                    reward = int(wf.content)
                    cur.execute("SELECT * FROM ggevent")
                    checker = cur.fetchall()
                    if str(checker) != "[]":
                        cur.execute("UPDATE ggevent SET reward=?", (reward,))
                        conn.commit()
                        await nachricht("Success, rewards for command gg.event have been set!", chan)
                    else:
                        cur.execute("INSERT INTO ggevent VALUES(?)", (reward,))
                        await nachricht("Success, rewards for command gg.event have been set!", chan)

                if com.startswith(" event autoevent1"):
                    chan = message.channel.id
                    await message.channel.send(content="Please send me the name from the event")
                    nam = await client.wait_for("message", check=c, timeout=None)
                    name = nam.content
                    await message.channel.send(content="Please send me now the description")
                    des = await client.wait_for("message", check=c, timeout=None)
                    desc = des.content
                    await nachricht("In how many days? (0, 1, ...)", chan)
                    day = await client.wait_for("message", check=c, timeout=None)
                    days = day.content
                    await nachricht("In how many hour's?", chan)
                    hour = await client.wait_for("message", check=c, timeout=None)
                    houre = hour.content
                    await nachricht("In how many minutes?", chan)
                    min = await client.wait_for("message", check=c, timeout=None)
                    minutes = min.content
                    await nachricht("Please send me now the gg token reward", chan)
                    re = await client.wait_for("message", check=c, timeout=None)
                    reward = re.content
                    e = await autev1(name, desc, days, houre, minutes, reward)
                    if e != False:
                        await sendmsg("Successfully Created autoevent 1", chan, 20)
                    else:
                        await sendmsg("Unsuccessfully Created autoevent 1, please try again", chan, 40)

                elif com.startswith(" event autoevent2"):
                    chan = message.channel.id
                    await message.channel.send(content="Please send me the name from the event")
                    nam = await client.wait_for("message", check=c, timeout=None)
                    name = nam.content
                    await message.channel.send(content="Please send me now the description")
                    des = await client.wait_for("message", check=c, timeout=None)
                    desc = des.content
                    await nachricht("In how many days? (0, 1, ...)", chan)
                    day = await client.wait_for("message", check=c, timeout=None)
                    days = day.content
                    await nachricht("In how many hour's?", chan)
                    hour = await client.wait_for("message", check=c, timeout=None)
                    houre = hour.content
                    await nachricht("In how many minutes?", chan)
                    min = await client.wait_for("message", check=c, timeout=None)
                    minutes = min.content
                    await nachricht("Please send me now the gg token reward")
                    re = await client.wait_for("message", check=c, timeout=None)
                    reward = re.content
                    e = await autev2(name, desc, days, houre, minutes, reward)
                    if e != False:
                        await sendmsg("Successfully Created autoevent 2", chan, 20)
                    else:
                        await sendmsg("Unsuccessfully Created autoevent 2, please try again", chan, 40)

                elif com.startswith(" event remove"):
                    chan = message.channel.id
                    await nachricht("Do you want remove autoevent 1 or 2 (just send me 1 or 2)", chan)
                    whi = await client.wait_for("message", check=c, timeout=None)
                    which = whi.content
                    if which=="1":
                        await nachricht("Are you sure to delete the autoevent 1? (y/n)", chan)
                        yo = await client.wait_for("message", check=c, timeout=None)
                        yon = yo.content
                        if yon=="y":
                            await autev1("Stoped", "removed autoevent1", 0, 0, 0, 0)
                            await nachricht("removes autoevent 1 events", chan)
                        else:
                            await nachricht("Didnt removed autoevent 1", chan)
                            pass
                    elif which=="2":
                        await nachricht("Are you sure to delete the autoevent 2? (y/n)", chan)
                        yo = await client.wait_for("message", check=c, timeout=None)
                        yon = yo.content
                        if yon == "y":
                            await autev2("Stoped", "removed autoevent 2", 0, 0, 0, 0)
                            await nachricht("removes autoevent 2 events", chan)
                        else:
                            await nachricht("Didnt removed autoevent 2", chan)
                            pass

                elif com.startswith(" adminlist add"):
                    chan = message.channel.id
                    await nachricht("Please send me now the userid from the user i should add to the admin list", chan)
                    yo = await client.wait_for("message", check=c, timeout=None)
                    yon = yo.content
                    guigui = client.get_guild(message.guild.id)
                    usr = guigui.get_member(int(yon))
                    arole = discord.utils.get(message.guild.roles, id=411811474780979201)
                    usr = guigui.get_member(int(yon))
                    arole = discord.utils.get(message.guild.roles, id=411811516954836993)
                    await usr.add_roles(arole, reason="Was added to the mod list")
                    await usr.add_roles(arole, reason="Was added to the admin list")
                    await nachricht("Admin Successfully added", chan)

                elif com.startswith(" adminlist list"):
                    chan = message.channel.id
                    nach = "These members could use the admin commands:\n"
                    arole = discord.utils.get(message.guild.roles, id=411811474780979201)
                    for meb in arole.members:
                        nach = nach+meb.name+"\n"
                    await nachricht(nach, chan)

                elif com.startswith(" adminlist remove"):
                    chan = message.channel.id
                    await nachricht("Please send me now the userid from the user i should remove from the admin list", chan)
                    yo = await client.wait_for("message", check=c, timeout=None)
                    yon = yo.content
                    guigui = client.get_guild(message.guild.id)
                    usr = guigui.get_member(int(yon))
                    arole = discord.utils.get(message.guild.roles, id=411811474780979201)
                    await usr.remove_roles(arole, reason="Was removed from the admin list")
                    await nachricht("Admin Successfully removed", chan)

                elif com.startswith(" modlist add"):
                    chan = message.channel.id
                    await nachricht("Please send me now the userid from the user i should add to the mod list", chan)
                    yo = await client.wait_for("message", check=c, timeout=None)
                    yon = yo.content
                    guigui = client.get_guild(message.guild.id)
                    usr = guigui.get_member(int(yon))
                    arole = discord.utils.get(message.guild.roles, id=411811516954836993)
                    await usr.add_roles(arole, reason="Was added to the mod list")
                    await nachricht("Mod Successfully added", chan)

                elif com.startswith(" modlist list"):
                    chan = message.channel.id
                    nach = "These members could use the mod commands:\n"
                    arole = discord.utils.get(message.guild.roles, id=411811516954836993)
                    for meb in arole.members:
                        nach = nach+meb.name+"\n"
                    await nachricht(nach, chan)

                elif com.startswith(" modlist remove"):
                    chan = message.channel.id
                    await nachricht("Please send me now the userid from the user i should remove from the mod list", chan)
                    yo = await client.wait_for("message", check=c, timeout=None)
                    yon = yo.content
                    guigui = client.get_guild(message.guild.id)
                    usr = guigui.get_member(int(yon))
                    arole = discord.utils.get(message.guild.roles, id=411811474780979201)
                    await usr.remove_roles(arole, reason="Was removed from the mod list")
                    await nachricht("Mod Successfully removed", chan)

            if invoke == "giftggtoken" and message.guild.owner_id == message.author.id:
                def c(m):
                    if m.author.id == message.author.id and m.channel.id == message.channel.id:
                        return m
                chan = message.channel.id
                await nachricht("Please send me now the id from the user you want to add the ggtokens", chan)
                yo = await client.wait_for("message", check=c, timeout=None)
                yon = yo.content
                await nachricht("How many tokens should i add?", chan)
                tok = await client.wait_for("message", check=c, timeout=None)
                token = int(tok.content)
                cur.execute("SELECT ggtokens FROM tokens WHERE userid=?", (int(yon),))
                ex = cur.fetchall()
                if str(ex) == "[]":
                    cur.execute("INSERT INTO tokens VALUES(?, ?)", (int(yon), token))
                    conn.commit()
                    await nachricht("Success, GG Tokens have been sent!", chan)
                else:
                    cur.execute("SELECT ggtokens FROM tokens WHERE userid=?", (int(yon),))
                    toke = cur.fetchone()[0]
                    newtoken = int(toke)+token
                    cur.execute("UPDATE tokens SET ggtokens=? WHERE userid=?", (newtoken, int(yon)))
                    conn.commit()
                    await nachricht("Success, GG Tokens have been sent!", chan)

            elif invoke == "takeggtoken" and message.guild.owner_id == message.author.id:
                def c(m):
                    if m.author.id == message.author.id and m.channel.id == message.channel.id:
                        return m
                chan = message.channel.id
                await nachricht("Please send me now the id from the user you want to remove the ggtokens", chan)
                yo = await client.wait_for("message", check=c, timeout=None)
                yon = yo.content
                await nachricht("How many tokens should i remove?", chan)
                tok = await client.wait_for("message", check=c, timeout=None)
                token = int(tok.content)
                cur.execute("SELECT ggtokens FROM tokens WHERE userid=?", (int(yon),))
                ex = cur.fetchall()
                if str(ex) == "[]":
                    await nachricht("Cant remove the user the tokens, because this user doesnt have tokens", chan)
                else:
                    cur.execute("SELECT ggtokens FROM tokens WHERE userid=?", (int(yon),))
                    toke = cur.fetchone()[0]
                    newtoken = int(toke)-token
                    if newtoken > 0:
                        cur.execute("UPDATE tokens SET ggtokens=? WHERE userid=?", (newtoken, int(yon)))
                        conn.commit()
                        await nachricht("Success, GG Tokens have been removed!", chan)
                    else:
                        await nachricht("Sorry, i cant remove this user this amount, because the user dosnt have %s tokens "%(token), chan)

            # @everyone
            if invoke == "tokenmember":
                yon = (message.content).replace("gg.tokenmember", "")
                chan = message.channel.id
                if yon != "":
                    cur.execute("SELECT ggtokens FROM tokens WHERE userid=?", (int(yon),))
                    ex = cur.fetchall()
                    if str(ex) == "[]":
                        await nachricht("this user doesnt have tokens", chan)
                    else:
                        cur.execute("SELECT ggtokens FROM tokens WHERE userid=?", (int(yon),))
                        toke = cur.fetchone()[0]
                        await message.channel.send(content="The User has %s ggtokens" % (toke))
                else:
                    await message.channel.sennd(content="gg.tokenmember [id]")
            elif invoke == "nextevent":
                try:
                    chan = message.channel.id
                    if evtitle != "NO" or len(evtitle) != 0:
                        await nachricht("The next Event %s is in %sd %sh %sm" % (evtitle, str(evd), str(evh), str(evm)), chan)
                    else:
                        await nachricht("No event scheduled", chan)
                except NameError:
                    chan = message.channel.id
                    await nachricht("No event scheduled", chan)

            # owner, admins
            elif invoke=="event":
                def c(m):
                    if m.author.id == message.author.id and m.channel.id == message.channel.id:
                        return m
                if message.guild.owner_id == message.author.id:
                    chan = message.channel.id
                    await nachricht("Please send me now the name for the event", chan)
                    nam = await client.wait_for("message", check=c, timeout=None)
                    name = nam.content
                    await nachricht("Please send me now the description for the event %s" % (name,), chan)
                    des = await client.wait_for("message", check=c, timeout=None)
                    desc = des.content
                    await nachricht("In how many day's? (0, 1, ...)", chan)
                    day = await client.wait_for("message", check=c, timeout=None)
                    days = day.content
                    await nachricht("In how many hour's?", chan)
                    hour = await client.wait_for("message", check=c, timeout=None)
                    houre = hour.content
                    await nachricht("In how many minute's?", chan)
                    min = await client.wait_for("message", check=c, timeout=None)
                    minutes = min.content
                    cur.execute("SELECT * FROM ggevent")
                    checker = cur.fetchall()
                    if str(checker) != "[]":
                        cur.execute("SELECT reward FROM ggevent")
                        reward = cur.fetchone()[0]
                        await ev(name, desc, days, houre, minutes, reward)
                        await nachricht(
                            "Congratulations your event has been created and timer will now be displayed! Use gg.announce event to annouce the new event",
                            chan)
                    else:
                        await nachricht(
                            "Unable to create event, Please try again. ERROR: No reward created with gg.setup event newevent",
                            chan)
                else:
                    chan = message.channel.id
                    arole = discord.utils.get(message.guild.roles, id=411811474780979201)
                    for meb in arole.members:
                        if meb.id == message.author.id:
                            await nachricht("Please send me now the name for the event", chan)
                            nam = await client.wait_for("message", check=c, timeout=None)
                            name = nam.content
                            await nachricht("Please send me now the description for the event %s" % (name,), chan)
                            des = await client.wait_for("message", check=c, timeout=None)
                            desc = des.content
                            await nachricht("In how many day's? (0, 1, ...)", chan)
                            day = await client.wait_for("message", check=c, timeout=None)
                            days = day.content
                            await nachricht("In how many hour's?", chan)
                            hour = await client.wait_for("message", check=c, timeout=None)
                            houre = hour.content
                            await nachricht("In how many minute's?", chan)
                            min = await client.wait_for("message", check=c, timeout=None)
                            minutes = min.content
                            cur.execute("SELECT * FROM ggevent")
                            checker = cur.fetchall()
                            if str(checker) != "[]":
                                cur.execute("SELECT reward FROM ggevent")
                                reward = cur.fetchone()[0]
                                await ev(name, desc, days, houre, minutes, reward)
                                await nachricht("Congratulations your event has been created and timer will now be displayed! Use gg.announce event to annouce the new event", chan)
                            else:
                                await nachricht("Unable to create event, Please try again. ERROR: No reward created with gg.setup event newevent", chan)

            elif invoke == "king":
                chan = message.channel.id
                if message.guild.owner_id == message.author.id:

                    def c(m):
                        if m.author.id == message.author.id and m.channel.id == message.channel.id:
                            return m

                    await nachricht("Please send me now the member id from the member i should add the role", chan)
                    memid = await client.wait_for("message", check=c, timeout=None)
                    meid = int(memid.content)
                    # cur.execute("CREATE TABLE IF NOT EXISTS ggking (role INTEGER, rrole INTEGER)")
                    cur.execute("SELECT role FROM ggking")
                    xy = cur.fetchall()
                    try:
                        if str(xy) != "[]":
                            cur.execute("SELECT role FROM ggking")
                            rid = cur.fetchone()[0]
                            roleid = int(rid)
                            arole = discord.utils.get(message.guild.roles, id=roleid)
                            mem = message.guild.get_member(meid)
                            await mem.add_roles(arole, reason="gg.king by " + message.author.name)
                            await nachricht("Congratulations %s you have won the the King Role till the next King Event! You have now access to your own chat room and voice channel for you and your team!" % (mem.mention), 392983553912209411)
                        else:
                            await nachricht("No role defined in gg.setup", chan)
                    except Exception as e:
                        await nachricht("Unable to set King Role to member ERROR: " + str(e), chan)
                else:
                    arole = discord.utils.get(message.guild.roles, id=411811474780979201)
                    for meb in arole.members:
                        if meb.id == message.author.id:
                            def c(m):
                                if m.author.id == message.author.id and m.channel.id == message.channel.id:
                                    return m

                            await nachricht("Please send me now the member id from the member i should add the role", chan)
                            memid = await client.wait_for("message", check=c, timeout=None)
                            meid = int(memid.content)
                            # cur.execute("CREATE TABLE IF NOT EXISTS ggking (role INTEGER, rrole INTEGER)")
                            cur.execute("SELECT role FROM ggking")
                            xy = cur.fetchall()
                            try:
                                if str(xy) != "[]":
                                    cur.execute("SELECT role FROM ggking")
                                    rid = cur.fetchone()[0]
                                    roleid = int(rid)
                                    arole = discord.utils.get(message.guild.roles, id=roleid)
                                    mem = message.guild.get_member(meid)
                                    await mem.add_roles(arole, reason="gg.king by " + message.author.name)
                                    await nachricht(
                                        "Congratulations %s you have won the the King Role till the next King Event! You have now access to your own chat room and voice channel for you and your team!" % (
                                            mem.mention), 392983553912209411)
                                else:
                                    await nachricht("No role defined in gg.setup", chan)
                            except Exception as e:
                                await nachricht("Unable to set King Role to member ERROR: " + str(e), chan)

            elif invoke == "winner":
                arole = discord.utils.get(message.guild.roles, id=411811474780979201)
                for meb in arole.members:
                    if meb.id == message.author.id:
                        def c(m):
                            if m.author.id == message.author.id and m.channel.id == message.channel.id:
                                return m
                        await message.channel.send(content="Please send me the userid From the winner")
                        cid = await client.wait_for("message", check=c, timeout=None)
                        id = cid.content
                        usr = message.guild.get_member(int(id))
                        print(usr)
                        await nachricht("Congratulations to %s on winning the Event! You have been rewarded with 100 GG Tokens!" % (usr.mention), 411821497578029056)


            elif invoke=="banner":
                arole = discord.utils.get(message.guild.roles, id=411811516954836993)
                for meb in arole.members:
                    if meb.id == message.author.id:
                        def c(m):
                            if m.author.id == message.author.id and m.channel.id == message.channel.id:
                                return m
                        await message.channel.send("Please send me now the header")
                        url = await client.wait_for("message", check=c, timeout=None)
                        await message.channel.send("Please send me now the text for the message")
                        text = await client.wait_for("message", check=c, timeout=None)
                        chan = message.guild.get_channel(392983553912209411)
                        await chan.send(content="**%s**\n%s" % (url.content, text.content))

            elif invoke=="tokenpayup":
                arole = discord.utils.get(message.guild.roles, id=411811516954836993)
                for meb in arole.members:
                    if meb.id == message.author.id:
                        adminchan = message.guild.get_channel(415845094521044992)
                        await adminchan.send(content="You are required to do a gg.token or gg.tokenreward @here")
                        await nachricht("An admin has been messaged regarding the Token Prize.", message.channel.id)
            elif invoke == "rking":
                chan = message.channel.id
                if message.guild.owner_id == message.author.id:
                    def c(m):
                        if m.author.id == message.author.id and m.channel.id == message.channel.id:
                            return m
                    await nachricht("Please send me now the member id from the member i should remove the role", chan)
                    memid = await client.wait_for("message", check=c, timeout=None)
                    meid = int(memid.content)
                    # cur.execute("CREATE TABLE IF NOT EXISTS ggking (role INTEGER, rrole INTEGER)")
                    cur.execute("SELECT rrole FROM ggking")
                    xy = cur.fetchall()
                    try:
                        if str(xy) != "[]":
                            cur.execute("SELECT rrole FROM ggking")
                            rid = cur.fetchone()[0]
                            roleid = int(rid)
                            arole = discord.utils.get(message.guild.roles, id=roleid)
                            mem = message.guild.get_member(meid)
                            await mem.remove_roles(arole, reason="gg.king by " + message.author.name)
                            await nachricht(
                                "It’s time to pass the title on %s you have been removed from the King Role!" % (
                                    mem.mention), 392983553912209411)
                        else:
                            await nachricht("No role defined in gg.setup", chan)
                    except Exception as e:
                        await nachricht("Unable to set King Role to member ERROR: " + str(e), chan)
                else:
                    arole = discord.utils.get(message.guild.roles, id=411811474780979201)
                    for meb in arole.members:
                        if meb == message.author.id:
                            def c(m):
                                if m.author.id == message.author.id and m.channel.id == message.channel.id:
                                    return m
                            await nachricht(
                                "Please send me now the member id from the member i should remove the role",
                                chan)
                            memid = await client.wait_for("message", check=c, timeout=None)
                            meid = int(memid.content)
                            # cur.execute("CREATE TABLE IF NOT EXISTS ggking (role INTEGER, rrole INTEGER)")
                            cur.execute("SELECT rrole FROM ggking")
                            xy = cur.fetchall()
                            try:
                                if str(xy) != "[]":
                                    cur.execute("SELECT rrole FROM ggking")
                                    rid = cur.fetchone()[0]
                                    roleid = int(rid)
                                    arole = discord.utils.get(message.guild.roles, id=roleid)
                                    mem = message.guild.get_member(meid)
                                    await mem.remove_roles(arole, reason="gg.king by " + message.author.name)
                                    await nachricht(
                                        "It’s time to pass the title on %s you have been removed from the King Role!" % (
                                            mem.mention), 392983553912209411)
                                else:
                                    await nachricht("No role defined in gg.setup", chan)
                            except Exception as e:
                                await nachricht("Unable to set King Role to member ERROR: " + str(e), chan)
            elif invoke=="eventannounce":
                arole = discord.utils.get(message.guild.roles, id=411811516954836993)
                for meb in arole.members:
                    if meb.id == message.author.id:
                        await message.channel.send(content="The next event is in %s days and in %sh:%sm" % (str(evd), str(evh), str(evm)))

            elif invoke=="revent":
                arole = discord.utils.get(message.guild.roles, id=411811516954836993)
                for meb in arole.members:
                    if meb.id == message.author.id:
                        getguid = client.get_guild(392983553912209409)
                        win = random.randint(0, len(getguid.members))
                        counter = 0
                        for memb in getguid.members:
                            if counter == win:
                                await message.channel.send(content="Hey %s you have won the revent :tada:" % (memb.mention))
                            counter += 1
            elif invoke=="store":
                def c(m):
                    if m.author.id == message.author.id and m.channel.id == message.channel.id:
                        return m
                await message.channel.send("Which of the 5 Shop items would you like to buy?")
                ent = await client.wait_for("message", check=c, timeout=None)
                if ent=="1":
                    try:
                        cur.execute("SELECT preis FROM store1")
                        preis = cur.fetchone()[0]
                        cur.execute("SELECT ggtokens FROM tokens WHERE userid=?", (message.author.id,))
                        tokens = cur.fetchone()[0]
                        if tokens-preis > 0:
                            await message.channel.send("Are you sure you want to buy this? Y/N")
                            yn = await client.wait_for("message", check=c, timeout=None)
                            if yn.content == "y":
                                tzt = tokens-preis
                                cur.execute("UPDATE tokens SET ggtokens=? WHERE userid=?", (tzt, message.author.id))
                                conn.commit()
                                code=str(random.randint(0, 9))+str(random.randint(0, 9))+random.choice(string.ascii_uppercase)
                                await message.author.send(content="Succesfull! Your Code is: %s" % (code))
                                adminchan = message.guild.get_channel(415845094521044992)
                                await adminchan.send(content="The User %s has generated the code `%s` for the store1" % (message.author.name, code))
                    except:
                        await message.channel.send(
                            content="Either this entry has not been made or you don't have enough money.")
                elif ent == "2":
                    try:
                        cur.execute("SELECT preis FROM store2")
                        preis = cur.fetchone()[0]
                        cur.execute("SELECT ggtokens FROM tokens WHERE userid=?", (message.author.id,))
                        tokens = cur.fetchone()[0]
                        if tokens - preis > 0:
                            await message.channel.send("Are you sure you want to buy this? Y/N")
                            yn = await client.wait_for("message", check=c, timeout=None)
                            if yn.content == "y":
                                tzt = tokens - preis
                                cur.execute("UPDATE tokens SET ggtokens=? WHERE userid=?", (tzt, message.author.id))
                                conn.commit()
                                code = str(random.randint(0, 9)) + str(random.randint(0, 9)) + random.choice(
                                    string.ascii_uppercase)
                                await message.author.send(content="Succesfull! Your Code is: %s" % (code))
                                adminchan = message.guild.get_channel(415845094521044992)
                                await adminchan.send(
                                    content="The User %s has generated the code `%s` for the store1" % (
                                    message.author.name, code))
                    except:
                        await message.channel.send(content="Either this entry has not been made or you don't have enough money.")
                elif ent == "3":
                    try:
                        cur.execute("SELECT preis FROM store3")
                        preis = cur.fetchone()[0]
                        cur.execute("SELECT ggtokens FROM tokens WHERE userid=?", (message.author.id,))
                        tokens = cur.fetchone()[0]
                        if tokens - preis > 0:
                            await message.channel.send("Are you sure you want to buy this? Y/N")
                            yn = await client.wait_for("message", check=c, timeout=None)
                            if yn.content == "y":
                                tzt = tokens - preis
                                cur.execute("UPDATE tokens SET ggtokens=? WHERE userid=?", (tzt, message.author.id))
                                conn.commit()
                                code = str(random.randint(0, 9)) + str(random.randint(0, 9)) + random.choice(
                                    string.ascii_uppercase)
                                await message.author.send(content="Succesfull! Your Code is: %s" % (code))
                                adminchan = message.guild.get_channel(415845094521044992)
                                await adminchan.send(
                                    content="The User %s has generated the code `%s` for the store1" % (
                                    message.author.name, code))
                    except:
                        await message.channel.send(content="Either this entry has not been made or you don't have enough money.")
                elif ent == "4":
                    try:
                        cur.execute("SELECT preis FROM store4")
                        preis = cur.fetchone()[0]
                        cur.execute("SELECT ggtokens FROM tokens WHERE userid=?", (message.author.id,))
                        tokens = cur.fetchone()[0]
                        if tokens - preis > 0:
                            await message.channel.send("Are you sure you want to buy this? Y/N")
                            yn = await client.wait_for("message", check=c, timeout=None)
                            if yn.content == "y":
                                tzt = tokens - preis
                                cur.execute("UPDATE tokens SET ggtokens=? WHERE userid=?", (tzt, message.author.id))
                                conn.commit()
                                code = str(random.randint(0, 9)) + str(random.randint(0, 9)) + random.choice(
                                    string.ascii_uppercase)
                                await message.author.send(content="Succesfull! Your Code is: %s" % (code))
                                adminchan = message.guild.get_channel(415845094521044992)
                                await adminchan.send(
                                    content="The User %s has generated the code `%s` for the store1" % (
                                    message.author.name, code))
                    except:
                        await message.channel.send(content="Either this entry has not been made or you don't have enough money.")
                elif ent == "5":
                    try:
                        cur.execute("SELECT preis FROM store5")
                        preis = cur.fetchone()[0]
                        cur.execute("SELECT ggtokens FROM tokens WHERE userid=?", (message.author.id,))
                        tokens = cur.fetchone()[0]
                        if tokens - preis > 0:
                            await message.channel.send("Are you sure you want to buy this? Y/N")
                            yn = await client.wait_for("message", check=c, timeout=None)
                            if yn.content == "y":
                                tzt = tokens - preis
                                cur.execute("UPDATE tokens SET ggtokens=? WHERE userid=?", (tzt, message.author.id))
                                conn.commit()
                                code = str(random.randint(0, 9)) + str(random.randint(0, 9)) + random.choice(
                                    string.ascii_uppercase)
                                await message.author.send(content="Succesfull! Your Code is: %s" % (code))
                                adminchan = message.guild.get_channel(415845094521044992)
                                await adminchan.send(
                                    content="The User %s has generated the code `%s` for the store1" % (
                                    message.author.name, code))
                    except:
                        await message.channel.send(content="Either this entry has not been made or you don't have enough money.")

            elif invoke=="vote":
                def c(m):
                    if m.author.id == message.author.id and m.channel.id == message.channel.id:
                        return m
                arole = discord.utils.get(message.guild.roles, id=411811474780979201)
                for meb in arole.members:
                    if meb.id == message.author.id:
                        await message.channel.send(content="Please send me now the heading")
                        heading = await client.wait_for("message", check=c, timeout=None)
                        await message.channel.send(content="Please send me now the description")
                        des = await client.wait_for("message", check=c, timeout=None)
                        await message.channel.send(content="Please send me now how many users could vote")
                        votes = await client.wait_for("message", check=c, timeout=None)
                        chan = message.guild.get_channel(416862932249608192)
                        msg = await chan.send(content="**%s**\n%s" % (heading.content, des.content))
                        await msg.add_reaction("✅")
                        await msg.add_reaction("❌")
                        cur.execute("SELECT canvote FROM voting")
                        ex = cur.fetchall()
                        if str(ex) != "[]":
                            cur.execute("UPDATE voting SET canvote=?, hasvoted=?", (int(votes.content), 0))
                            conn.commit()
                        else:
                            cur.execute("INSERT INTO voting (canvote) VALUES(?)", (int(votes.content),))
                            conn.commit()
                        # EXAMPLE
                        '''
            elif invoke=="event":
                def c(m):
                    if m.author.id == message.author.id and m.channel.id == message.channel.id:
                        return m
                if message.guild.owner_id == message.author.id:
                   
                else:
                    for meb in arole.members:
                        if meb.id == message.author.id:
                                
                        '''

    async def on_raw_reaction_add(self, emoji, message_id, channel_id, user_id):
        if channel_id == 416862932249608192:
            if str(emoji) == "✅":
                cur.execute("SELECT hasvoted FROM voting")
                ex = cur.fetchall()
                if str(ex) != "[]":
                    cur.execute("SELECT hasvoted FROM voting")
                    vo = cur.fetchone()[0]
                    vos = int(vo)+1
                    cur.execute("UPDATE voting SET hasvoted=?", (vos,))
                    conn.commit()
                    cur.execute("SELECT canvote FROM voting")
                    maxvo = cur.fetchone()[0]
                    print(maxvo)
                    print(vo)
                    if maxvo == vo:
                        gu = client.get_channel(channel_id)
                        guild = gu.guild.id
                        gugui = client.get_guild(guild)
                        await gu.send(content="Voting has ended!")
                else:
                    cur.execute("INSERT INTO voting (hasvoted) VALUES(?)", (1,))
                    conn.commit()

            else:
                cur.execute("SELECT hasvoted FROM voting")
                ex = cur.fetchall()
                if str(ex) != "[]":
                    cur.execute("SELECT hasvoted FROM voting")
                    vo = cur.fetchone()[0]
                    vos = int(vo) + 1
                    cur.execute("UPDATE voting SET hasvoted=?", (vos,))
                    conn.commit()
                    cur.execute("SELECT canvote FROM voting")
                    maxvo = cur.fetchone()[0]
                    if maxvo == vo:
                        gu = client.get_channel(channel_id)
                        guild = gu.guild.id
                        gugui = client.get_guild(guild)
                        await gu.send(content="Voting has ended!")
                else:
                    cur.execute("INSERT INTO voting (hasvoted) VALUES(?)", (1,))
                    conn.commit()

    async def on_raw_reaction_remove(self, emoji, message_id, channel_id, user_id):
        if channel_id == 416862932249608192:
            if str(emoji) == "✅":
                cur.execute("SELECT hasvoted FROM voting")
                ex = cur.fetchall()
                if str(ex) != "[]":
                    cur.execute("SELECT hasvoted FROM voting")
                    vo = cur.fetchone()[0]
                    vos = int(vo) - 1
                    cur.execute("UPDATE voting SET hasvoted=?", (vos,))
                    conn.commit()
                else:
                    ch = await client.get_user(250055619107749888)
                    await ch.send(content="Sorry! The voting doesnt work because there is a reaction removed but no reaction was added")
            else:
                cur.execute("SELECT hasvoted FROM voting")
                ex = cur.fetchall()
                if str(ex) != "[]":
                    cur.execute("SELECT hasvoted FROM voting")
                    vo = cur.fetchone()[0]
                    vos = int(vo) - 1
                    cur.execute("UPDATE voting SET hasvoted=?", (vos,))
                    conn.commit()
                else:
                    ch = await client.get_user(250055619107749888)
                    await ch.send(content="Sorry! The voting doesnt work because there is a reaction removed but no reaction was added")


client = MyClient()
client.run(KEYS.TOKEN)
