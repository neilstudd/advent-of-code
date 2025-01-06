# 2024 AI Experiment

As with a lot of domains, Advent of Code has seen a mixture of fascination 
and backlash about the emergence of generative AI and code completion tools, 
predominantly focused on those who have been using LLMs to "cheat" the global 
leaderboards.

I've mostly been an AoC purist prior to 2024, with my [AoC Readme](README.md) 
showing only a couple of occaions when I'd turned to AI tooling for help when I 
got totally stumped, but I'd left it mostly off-limits. Consequently, my 2022 
and 2023 runs were relatively patchy: I'm not a programmer by profession, and at 
a certain point (usually when the knowledge of specific algorithms or approaches 
to pathfinding came into play) I had to gracefully bow out.

That said, part of my day job involves educating new developers on the benefits 
and the pitfalls of AI tools, so educating myself on the subject is a must. A 
lot of my day-to-day work designing AI challenges involves working with deliberately 
simple problems, so for my 2024 Advent of Code run, I decided to see whether AI 
was getting better at solving more complex challenges.

Therefore, rather than starting my challenges by turning GitHub Copilot **off**, 
I instead began by making sure it was switched **on**. I still aimed to fully 
solve the problems for myself, but Copilot's completions were available for me 
on-demand, so that I was effectively pairing with Copilot for much of December.

### Why?

As I touched upon above, my main reasons for this "AI-first" approach were:

* To assist in my AI curriculum creation process, by seeing how well AI tools could handle more complex problems.
* To test my own problem decomposition skills: even if I don't know the code that I need, can I describe the problem in a way that an AI can understand?
* To evaluate for myself whether code completion tools are improving, and whether they can be used as a learning tool rather than a crutch.

### What did I observe?

For better or worse, I found that Copilot was a huge help in 2024. The issues 
that I encountered tended to be reading comprehension problems (ironic, as much 
of the obfuscation in the challenge text is presumably to prevent AI tools from
being able to one-shot the puzzles). There were only three days where I failed 
to get the second star, and in all three cases, I can hold my hands up and 
unashamedly say "Nope, no idea how I'd even _begin_ to think about solving that".

Here are some of the patterns that I observed with Copilot and LLMs:

* **Input parsing wins:** While the puzzle input was usually in a format which was quite 
predictable, on days when the puzzle input was more complex - such as when it contained two different kinds of data (e.g. setup and instructions) - 
I found that giving the input sample and my desired output (e.g. specific named 
variables in a specific format), Copilot was able to generate the parsing code
with an almost 100% success rate. This speaks primarily to the power of examples.
* **Performance gains:** It's something of a running joke in my group's AoC 
Slack channels that I'll always take the brute-force approach to solving a problem 
if I can get away with it, and in previous years this has sometimes meant leaving 
my code running for an hour or longer to reach the correct answer! It's also been 
the reason why I've hit a wall in previous years, as I simply haven't been able 
to determine a more efficient way to structure my data/code. But Copilot really 
shone here; highlighting a section of code and just asking `optimise this` or 
`improve performance` would often instantly get me to the correct answer. However 
it was still erratic enough that it was important enough to design "expected outputs"
first, so that I could tell if the optimisation had the same behaviour as the previous 
code (there was at least one day when it felt that I was stuck between "run fast, but get 
the wrong answer" and "run slow, but it'll get the right answer... in about a week").
* **Algorithmic assistance:** Going hand-in-hand with the above, often the challenges 
are designed with a specific type of algorithm in mind for the solution, where (as 
a relatively novice programmer) I didn't even know how that algorithm existed, let 
alone how to implement it. There were 1-2 occasions when I observed hints on Reddit 
along the lines of "oh, you just need to use a Blah algorithm"; I'd then prompt
Copilot with "rewrite to use a Blah algorithm" and it would give me the code that I needed.
* **The danger of reinforcing errors:** We saw a lot of 2D grids in 2024 (finally 
prompting me to begin a library of common methods!), but I stumbled badly on the 
first couple, largely because me and my AI pair programmer kept conflating the 
x and y axes. Often I'd just assume that I was the one in the wrong, but whenever 
I saw something traversing a grid to the left when I'd expected it to be traversing 
upwards, it was often easier to scrap the 20-30 lines of code that we'd just paired 
on, and go through it more diligently on my own.

### Conclusion

One of the points that we often make when educating new developers about AI tools 
is that they won't necessarily help with your learning process: when learning, 
the goal isn't to reach the correct answer, it's to understand the process of 
getting to that answer. My gut feel is that this mostly still holds true: there
were a few days when I almost felt like I'd cheated myself, having executed a 
large section of machine-generated code which got me the answer, but where I 
didn't necessarily understand _why_.

That said, I used this feeling to guide my learning process! Whenever I had the 
feeling that I didn't quite understand why something had worked, I took the time 
to step through the code (often refactoring as I went) and, in doing so, gained 
a much better understanding of algorithms such as BFS/DFS which were hugely 
prevalent in 2024.

Also - and maybe this is because of my background in testing and quality! - I 
appreciated that one of the best ways to keep Copilot within its lane was to 
ensure that I'd prompted it with a set of examples, and (as the month went on)
encoded those as actual assertions, so that whenever I instructed Copilot to 
make changes, I could re-run my changes and see whether anything had broken.

**Will I take this same approach in 2025?** Probably not - the purist in me 
wants to focus more on the problem-solving! That said, I've got some other ideas 
for my 2025 run (including some streaming, and potentially doing a "strict TDD" 
run), and I might invent some kind of scoring system which rewards me for 
avoiding AI altogether, or penalises me when I find the need for it.