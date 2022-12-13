<h1>API</h1>
<h2>Background Context</h2>
<p>Old-school system administrators usually only know Bash and that is what they use to build their scripts. While Bash is perfectly fine for a lot of things, it can quickly get messy and not efficient compared to other programming languages. The new generation of system administrators, usually called SREs, are pretty much regular software engineers but instead of building products, they are managing systems. And one of the big differences with their predecessors is that they know more than just Bash scripting.</p>
<p>One popular way to expose an application and dataset is to use an API. Often, they are the public facing part of websites and micro-services so that allow outsiders to interact with them &ndash; access and modify their data. In this project, you will access employee data via an API to organize and export them to different data structures.</p>
<p>This is a perfect example of a task that is not suited for Bash scripting, so let&rsquo;s build Python scripts.</p>
<h2>Resources</h2>
<p><strong>Read or watch</strong>:</p>
<ul>
<li><a title="Friends don't let friends program in shell script" href="https://intranet.hbtn.io/rltoken/iRuX_VjIFuDLTdMpjJnSFw" target="_blank" rel="noopener">Friends don&rsquo;t let friends program in shell script</a></li>
<li><a title="What is an API" href="https://intranet.hbtn.io/rltoken/E7BTWmGqsMlvGfoiyvp3zA" target="_blank" rel="noopener">What is an API</a></li>
<li><a title="What is an API? In English, please" href="https://intranet.hbtn.io/rltoken/xfdvNo3t8Judw6CVCSZ48A" target="_blank" rel="noopener">What is an API? In English, please</a></li>
<li><a title="What is a REST API" href="https://intranet.hbtn.io/rltoken/8vtUsjExqwT9SypvpJGtSQ" target="_blank" rel="noopener">What is a REST API</a></li>
<li><a title="What are microservices" href="https://intranet.hbtn.io/rltoken/D_qjbDxkl2ZBr2v_AiO5Bw" target="_blank" rel="noopener">What are microservices</a></li>
<li><a title="PEP8 Python style - having a clean code respecting style guide is really appreciated in the industry" href="https://intranet.hbtn.io/rltoken/7SEHV4FrRLAPY9icO64Bwg" target="_blank" rel="noopener">PEP8 Python style - having a clean code respecting style guide is really appreciated in the industry</a></li>
</ul>
<h2>Learning Objectives</h2>
<p>At the end of this project, you are expected to be able to&nbsp;<a title="explain to anyone" href="https://intranet.hbtn.io/rltoken/-TUGK2dpC_TyUMZsb60KVQ" target="_blank" rel="noopener">explain to anyone</a>,&nbsp;<strong>without the help of Google</strong>:</p>
<h3>General</h3>
<ul>
<li>What Bash scripting should not be used for</li>
<li>What is an API</li>
<li>What is a REST API</li>
<li>What are microservices</li>
<li>What is the CSV format</li>
<li>What is the JSON format</li>
<li>Pythonic Package and module name style</li>
<li>Pythonic Class name style</li>
<li>Pythonic Variable name style</li>
<li>Pythonic Function name style</li>
<li>Pythonic Constant name style</li>
<li>Significance of CapWords or CamelCase in Python</li>
</ul>
<h2>Requirements</h2>
<h3>General</h3>
<ul>
<li>Allowed editors:&nbsp;<code>vi</code>,&nbsp;<code>vim</code>,&nbsp;<code>emacs</code></li>
<li>All your files will be interpreted/compiled on Ubuntu 14.04 LTS using&nbsp;<code>python3</code>&nbsp;(version 3.4.3)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly&nbsp;<code>#!/usr/bin/python3</code></li>
<li><strong>Libraries imported in your Python files must be organized in alphabetical order</strong></li>
<li>A&nbsp;<code>README.md</code>&nbsp;file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the&nbsp;<code>PEP 8</code>&nbsp;style</li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using&nbsp;<code>wc</code></li>
<li>All your modules should have a documentation (<code>python3 -c 'print(__import__("my_module").__doc__)'</code>)</li>
<li>You must use&nbsp;<a title="get" href="https://intranet.hbtn.io/rltoken/MgESLFGCZ7ufM1EOTJ6mWg" target="_blank" rel="noopener">get</a>&nbsp;to access to dictionary value by key (it won&rsquo;t throw an exception if the key doesn&rsquo;t exist in the dictionary)</li>
<li>Your code should not be executed when imported (by using&nbsp;<code>if __name__ == "__main__":</code>)</li>
</ul>
