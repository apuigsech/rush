import click
from configobj import ConfigObj

import openai
from chatgpt_wrapper import ChatGPT

from utils import config_overlay, input_config, transform_config
from input import Input
from transform import Transform

TEXT_SHORT = "I met a traveler from an antique land who said, Two vast and trunkless legs of stone stand in the desert. Near them, on the sand, half sunk, a shattered visage lies, Whose frown and wrinkled lip and sneer of cold command, While at its sculptor well those passions red which yet survive, Stamped on these lifeless things. The hand that muck them and the heart that fit, And on the pedestal these words appear, My name is Azimandius, King of Kings. Look on my works, he mighty and despair. Everything beside remains, round the decay of that colossal wreck, Boundless and bare, the lone and level sands stretch far away."
TEXT_LONG = "First of all, you need to know them for your own life. Because you gotta know that there are differences in intelligence. It's really important. If you go into a job and you're not smart enough for that job, you're gonna have one bloody miserable time. And you're gonna make life wretched for the people around you because you won't be able to handle the position. And as you climb hierarchies of competence, the demand on fluid intelligence increases. And so, unless you wanna fail, you don't put yourself in over your head. Well, what's over your head? Well, that's a tricky thing to figure out. I mean, you have to figure that out with intelligence. You have to figure it out with conscientiousness. You have to figure it out with creativity. You have to figure out with stress tolerance, with agreeableness, because you wanna go into a cooperative environment and not a competitive one if you're agreeable. And with neuroticism, you probably wanna keep the stress level of your job relatively low. Because those are all places that you can break down. And most people have at least one significant weakness in their intelligence personality makeup. And you gotta be careful not to place yourself in a position where that's gonna be a fatal flaw. But what you really wanna do, as far as I can tell, if you wanna maximize your chances for both success and let's say well-being, is you wanna find a strata of occupation in which you would have an intelligence that would put you in the upper quartile. That's perfect. Then you're a big fish in a small pond. And you don't wanna be the stupidest guy in the room. It's a bloody rough place to be. So, and you probably don't wanna be the smartest guy in the room either, is what that probably means is you should be in a different room. You should look at a place where, if you're right at the top, you've mastered it. It's time to go somewhere where you're a little lower so that you've got something to climb up for. So, and I can, if you're not hyper conscientious, for example, you're probably not gonna want a job that you have to work 70 hours a week at. Because you're just not wired up that way. You'd rather have some leisure and like more power to you. If that's how you're wired up, there's nothing wrong with having some leisure. But if you're someone who can't stand sitting around doing nothing ever, then maybe you can go into a job that's gonna require you to work 75 hours a week. And almost all jobs that are at the top of complex dominance hierarchies require very high intelligence and insane levels of conscientiousness. As well, generally speaking, as pretty damn high levels of stress tolerance. Cause that can knock you out too, because there's gonna be sharp fluctuations in your career, generally speaking, at the higher levels of a structure. And you have to make very complicated decisions, often with very short time horizons. So you have to decide if that's what you want. So, okay, so how smart do you have to be to be different things in life? Well, if you have an IQ of 116 to 130, which is 85th percentile and above, so it's one person in eight up to one person in 130, I believe is 85, 90, 95, is it 95? I think it's 95. One person in eight to one person in 20. Then you can be a attorney, a research analyst, an editor, an advertising manager, a chemist, an engineer, an executive manager, et cetera. That's the, now, that's not the high end for IQ, by the way. You know, that it can go up, well, it can go up indefinitely, although there's fewer and fewer people as it goes up. So, if you wanna be the best at what you're doing, bar none, then having an IQ of above 145 is a necessity. And maybe you're pushing 160 in some situations. And maybe that's making you one person in 10,000 or even one person in 100,000. And then also, to really be good at it, you probably have to be reasonably stressed, tolerant, and also somewhat conscientious. So, you know, people, you think, well, why is it that smart people are at the top of dominance hierarchies? And the answer to that, in part, is because they get there first, right? I mean, everything's a race, roughly speaking. And the faster you are, the more likely you are to be at the forefront of the pack. And intelligence in large part is speed. That's not all of it is. So, if you're moving towards something difficult, rapidly, the faster people are going to get there first. So, IQ of 110 to 115, so that's 73rd to 85th percentile. Copywriter, accountant, manager, sales manager, sales analyst, general manager, purchasing agent, registered nurse, sales account executive. If you look at universities, the smartest people are there above this. Who are the smartest people at university? What do you think? Mathematicians, physicists and mathematicians, right, right. I could tell you who's on the other end, but I won't. Ha ha ha ha ha ha ha ha ha ha ha ha ha ha ha ha. Yeah, I'd like to though. Anyways, okay, going down the, now 103 to 108 is slightly above average, right? 60th to 70th percentile. Store manager, bookkeeper, credit clerk, lab tester, general sales, telephone sales, accounting clerk, computer operator, customer service rep, technician, clerk, typist. So you see at this level, people have some technical skill and some ability to deal with complex things. Okay, that's dead average. Hundred is average. Dispatcher in a general office, police patrol officer, receptionist, cashier, general clerical, inside sales clerk, meter reader, printer, teller, data entry, electrical helper. 95th to 98th, machinist, food department manager, quality control checker, security guard, unskilled labor, maintenance, arc welder, die setter, mechanic. Good IQ range for relatively qualified tradespeople. 87 to 93. Messenger, factory production worker, assembler, food service worker, nurses aide, warehoseman, custodian, janitor, material handler, packer. Now what you're starting to see is that as you move down the hierarchy, the jobs get simpler. They're more likely to be assigned by other people or they're repetitive. Because what IQ predicts to some degree is how rapidly you can learn something, but once you've learned it, it doesn't predict how necessarily how well you do at it. And so the more repetitive jobs, people with lower IQs are more suited to more repetitive jobs. Under 87, is there something? Well, no. Right, that's a big problem. And it's something our society has not addressed at all. Jobs for people with IQs of less than 80% of less than 85 are very, very rare. So what the hell are those people supposed to do? It's like 15% of the population. What are they supposed to do? Well, we better figure it out because one of the things that's happening too is that as the high IQ tech geeks get a hold of the world, the demand for cognitive power is increasing, not decreasing, right? You wanna be a teller? Well, you know, those checkout machines, they're not so simple. You wanna work at McDonald's? You think that's a simple job? You don't see robots working at McDonald's. And the reason for that is that what McDonald's workers do is too complex for robots to do. So, well, so this is a discussion that no one wants to have, but that's okay. It's still a problem and it has to be dealt with. So the US government, I think I told you this at one point already, it's illegal to induct anyone into the US Army if they have an IQ of less than 83, right? It's about 10% of the population because the US Army, and they've been doing IQ testing since IQ testing began, because they want everybody they can possibly get into the Army because in peacetime, they use it as a way of moving people up the socioeconomic ladder and in wartime, well, obviously, you need as many soldiers as you can get your hands on. And so you're not gonna be any pickier than you have to be. So when the US Army says it's illegal to induct anybody into the armed forces, if they have an IQ of less than 83, then you know that they've done it for absolute necessity, right? And when people have made a finding that contradicts what they want to hear and they're doing it out of absolute necessity, you can be reasonably true that it's one of those facts that just won't bloody well go away. And so you might think, well, if there's nothing for someone with an IQ of less than 83 to do in the Army, what makes you think that there's something that they can do in the general population? And then the issue is, you know, because the conservatives will say, well, they should just work harder. It's like, sorry, that ain't gonna fly. And the liberals will say, well, there's no difference between people anyhow. And you can just train people to do everything. And that's wrong. So they're both wrong and they're seriously wrong. And the fact that neither side of the political perspective will take a good, cold, hard look at this problem means that we're going to increasingly have a structural problem in our societies because we're complexifying everything so rapidly that you can't find employment unless increasingly, unless you're intelligent. You guys are really gonna face this, you know, lawyers are disappearing like mad. And the reason for that is you can look it up online. Increasingly, you can do things yourself if you're smart. And so like the working class, people have been wiped out pretty nicely over the last 30 years by automation and various other things. It's the low end of the white collar class that's coming up next. So I'm not saying that lawyers are in the low end, but low end lawyers are in the low end of the white collar class. So there's still gonna be plenty of positions for people who are creative and fast on their feet and super smart. In fact, those people are gonna have all the money and that's already happening to a great degree."
TEXT_LONG_ES = "De acuerdo con Elon Musk, un gobierno mundial podría conducirnos al colapso de la humanidad. ¿Por qué razón? Veámoslo. Desde 2013 se celebra anualmente en Dubai el World Government Summit, algo así como el Encuentro Mundial de los Gobiernos, un foro que pretende estrechar los lazos de cooperación entre los distintos estados del planeta para acercarnos a una acción política coordinada, como aquella que podría tener lugar bajo un solo gobierno mundial. Pues bien, en la edición de este año ha participado, telemáticamente eso sí, Elon Musk, consejero delegado de Tesla, pero también consejero delegado de Twitter. Y en este foro mundial de los gobiernos, en este foro que pretende acercarnos poquito a poco a una especie de gobierno mundial, Elon Musk ha lanzado un mensaje muy importante. Escuchemoslo. Lo que es más que está diciendo atención que un exceso de cooperación entre gobiernos acercarnos demasiado a un único gobierno mundial podría entrañar un riesgo existencial para la civilización humana. Es decir, que la civilización humana podría extinguirse bajo la bota de un único gobierno mundial. ¿Y por qué hace una afirmación tan aparentemente hiperbólica que justificaría, según Musk, la gravedad de sus palabras? Más que está diciendo que a lo largo de la historia de la humanidad, el hecho de que hayan existido diversas civilizaciones separadas cultural y territorialmente, es decir, el amplio grado de descentralización civilizatoria ha permitido la diversidad y la heterogéneidad de esas civilizaciones humanas. Y la ventaja de que existan codo con codo diversos tipos de civilizaciones humanas, diversos gobiernos, si lo queremos, no unificados bajo una misma entidad global, la ventaja es que si una de esas civilizaciones colapsa por acumulación de errores internos, hay otras civilizaciones igualmente humanas que pueden no solo preservar aquellos elementos culturales de la civilización que está colapsando y que pueden ser funcionales y útiles para su civilización, sino que también pueden reemplazar y tomar el relevo histórico de esa civilización que colapsa. En cambio, si todo el mundo fuera una única civilización bajo la dirección de un mismo gobierno, si ese gobierno comete fallos sistemáticos que abocan a todos aquellos que se hay en bajo su jurisdicción al colapso, como solo hay un gobierno para todo el mundo, para toda la humanidad, ese colapso civilizatorio sería un colapso civilizatorio no solo de una cultura determinada, sino del conjunto de la humanidad. A quienes hayan leído el libro antifragil de Nacim Taleb, este argumento de Musk les recordará a algunas de las argumentaciones que desarrolló Taleb en su libro. Básicamente un sistema es más adaptativo a cualquier estrés externo, a cualquier perturbación, a cualquier shock al que se pueda enfrentar, si es un sistema cuyas partes son muy diversas y muy diferentes entre sí que cuando todas las partes de ese sistema son exactamente iguales. En el primer caso, cuando tenemos mucha diversidad interna, puede que el shock, la perturbación externa, mate a algunas de las partes internas del sistema. Pero también puede que otras partes sean capaces de resistir, sean muy adaptativas frente a ese shock externo y, por tanto, aunque algunas partes del sistema hayan muerto, el resto del sistema se puede reproducir, puede recolonizar las partes que han quedado desiertas, los que se han comportado peor ante ese shock externo pueden aprender o pueden heredar rasgos de aquellas otras partes que hayan sobrevivido a esa perturbación y, por tanto, con el tiempo el conjunto del sistema sobrevive y, además, todas sus partes aprenden o debienen capaces de soportar shocks externos similares al que previamente ha acabado con una parte del sistema. En cambio, si nos encontramos en el segundo escenario, cuando todas las partes del sistema son exactamente iguales, cuando todas las partes del sistema son una copia de una misma parte, basta con que haya una parte que no sea capaz de resistir esa perturbación externa para que todo el resto del sistema tampoco sea capaz de hacerlo, porque todas las partes de ese sistema son copias entre sí, son idénticas, por tanto, si falla uno necesariamente fallan todos. O en el extremo, si muere uno frente a una perturbación externa, mueren todos. Por eso, un sistema sin diversidad interna es un sistema poco adaptativo frente a cualquier perturbación externa. Y eso, en definitiva, es frente a lo que nos está advirtiendo Elon Musk, cuidado con avanzar hacia un solo gobierno mundial que apruebe reglas exactamente iguales en todas las partes del planeta, porque si esas leyes, esas normas, esas reglas son equivocadas, si son gravísimamente equivocadas, entonces toda la humanidad no una civilización, sino toda la humanidad corre el riesgo de desaparecer. En definitiva, la descentralización política a muy pequeña escala es un marco institucional indispensable para que ese mecanismo evolutivo tan importante como es la prueba y el error, el ensayo y el error no acabe extinguiendo a la propia humanidad, porque en todo mecanismo prueba error, aparecerán errores, aparecerán en ocasiones errores gravísimos, y lo fundamental es que podamos ponerle barreras a esos errores gravísimos, es decir, que los errores gravísimos solo afecten a aquellos que los han cometido, no al conjunto de la humanidad. Pero si solo tenemos un único gobierno mundial, que como todos los gobiernos experimenta con regulaciones y por tanto recurre al mecanismo de prueba y error, si el error que comete ese único gobierno mundial es gravísimo, se nos llevaría a todos por delante."


@click.command()
@click.option('-c', '--config', 'config_file', help='read config from a file', default='default.conf', type=click.Path(exists=True))
@click.option('--co', '--config-overlay', help='', type=(str, str), multiple=True)
@click.option('-i', '--input', 'input_url', help='input url', required=True)
@click.option('-t', '--transform', help='', type=click.Choice(['curate', 'translate', 'summarize', 'htmlclean', 'html2markdown']), multiple=True)

# @click.option('-o', '--output', help='output file', default='out', name='output')
# @click.option('--output.format', help='', type=click.Choice(['html', 'plain_html', 'mp3']), default='html', name='output_format')

def main(config_file, co, input_url, transform):
    try:
        config = ConfigObj(config_file)
    except Exception as e:
        print(f"Unable to read config: {str(e)}")
        exit(0)

    for keys,value in co:
        config = config_overlay(config, keys, value)

    text = Input(input_config(input_url, config)).get_text(input_url)

    for name in transform:
        text = Transform(name, transform_config(name, config)).apply(text)

    print(text)





if __name__ == '__main__':
    main()