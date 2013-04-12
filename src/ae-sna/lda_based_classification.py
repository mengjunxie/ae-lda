<!DOCTYPE html>
<html lang="en">
<head>
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <meta charset="utf-8">
  <title>
  h0cked / AE-SNA-Clean 
  / source  / src / ae-sna / lda_based_classification.py
 &mdash; Bitbucket
</title>
  <link rel="icon" type="image/png" href="https://d3oaxc4q5k2d6q.cloudfront.net/m/ab1188947552/img/favicon.png">
  <meta id="bb-canon-url" name="bb-canon-url" content="https://bitbucket.org">
  
  
<link rel="stylesheet" href="https://d3oaxc4q5k2d6q.cloudfront.net/m/ab1188947552/compressed/css/3be2819cb960.css" type="text/css" />
<link rel="stylesheet" href="https://d3oaxc4q5k2d6q.cloudfront.net/m/ab1188947552/compressed/css/ed56475b5627.css" type="text/css" />

  <!--[if lt IE 9]><link rel="stylesheet" href="https://d3oaxc4q5k2d6q.cloudfront.net/m/ab1188947552/css/aui/aui-ie.css" media="all"><![endif]-->
  <!--[if IE 9]><link rel="stylesheet" href="https://d3oaxc4q5k2d6q.cloudfront.net/m/ab1188947552/css/aui/aui-ie9.css" media="all"><![endif]-->
  <!--[if IE]><link rel="stylesheet" href="https://d3oaxc4q5k2d6q.cloudfront.net/m/ab1188947552/css/aui-overrides-ie.css" media="all"><![endif]-->
  <meta name="description" content=""/>
  <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="Bitbucket" />
  
  <link href="/h0cked/ae-sna-clean/rss?token=b979471dff22305caac516903f526a66" rel="alternate nofollow" type="application/rss+xml" title="RSS feed for AE-SNA-Clean" />

</head>
<body class="production "
      >
<script type="text/javascript" src="https://d3oaxc4q5k2d6q.cloudfront.net/m/ab1188947552/compressed/js/e98deabf8a2e.js"></script>
<div id="page">
  <div id="wrapper">
    
    <header id="header" role="banner">
      
        
      
      <nav class="aui-header aui-dropdown2-trigger-group" role="navigation">
        <div class="aui-header-inner">
          <div class="aui-header-primary">
            <h1 class="aui-header-logo aui-header-logo-bitbucket">
              <a href="/" class="aui-nav-imagelink" id="logo-link">
                <span class="aui-header-logo-device">Bitbucket</span>
              </a>
            </h1>
            
            <script id="repo-dropdown-template" type="text/html">
  

[[#hasViewed]]
  <div class="aui-dropdown2-section">
    <strong class="viewed">Recently viewed</strong>
    <ul class="aui-list-truncate">
      [[#viewed]]
        <li class="[[#is_private]]private[[/is_private]][[^is_private]]public[[/is_private]] repository">
          <a href="[[url]]" title="[[owner]]/[[name]]" class=" aui-icon-container">
            <img class="repo-avatar size16" src="[[{avatar}]]" alt="[[owner]]/[[name]] avatar"/>
            [[owner]] / [[name]]
          </a>
        </li>
      [[/viewed]]
    </ul>
  </div>
[[/hasViewed]]
[[#hasUpdated]]
<div class="aui-dropdown2-section">
  <strong class="updated">Recently updated</strong>
  <ul class="aui-list-truncate">
    [[#updated]]
    <li class="[[#is_private]]private[[/is_private]][[^is_private]]public[[/is_private]] repository">
      <a href="[[url]]" title="[[owner]]/[[name]]" class=" aui-icon-container">
        <img class="repo-avatar size16" src="[[{avatar}]]" alt="[[owner]]/[[name]] avatar"/>
        [[owner]] / [[name]]
      </a>
    </li>
    [[/updated]]
  </ul>
</div>
[[/hasUpdated]]

</script>
            <ul role="menu" class="aui-nav">
              
                <li>
                  <a class="aui-dropdown2-trigger aui-dropdown2-trigger selected"
                     aria-owns="repo-dropdown" aria-haspopup="true" href="/repo/mine " id="repositories-dropdown-trigger">
                    Repositories
                    <span class="aui-icon-dropdown"></span>
                  </a>
                  <nav id="repo-dropdown" class="aui-dropdown2 aui-style-default">
                    <div id="repo-dropdown-recent"></div>
                    <div class="aui-dropdown2-section">
                      <ul>
                        <li>
                          <a href="/repo/create" class="new-repository" id="create-repo-link">
                            Create repository
                          </a>
                        </li>
                        <li>
                          <a href="/repo/import" class="import-repository" id="import-repo-link">
                            Import repository
                          </a>
                        </li>
                      </ul>
                    </div>
                  </nav>
                </li>
                  <li>
                    <a class="aui-button aui-button-primary aui-style" href="/repo/create" id="repo-create-cta">
                      Create
                    </a>
                  </li>
              
            </ul>
            
          </div>
          <div class="aui-header-secondary">
            
            <ul role="menu" class="aui-nav">
              <li>
                <form action="/repo/all" method="get" class="aui-quicksearch">
                  <label for="search-query" class="assistive">owner/repository</label>
                  <input  id="search-query" class="search" type="text" placeholder="owner/repository" name="name">
                </form>
              </li>
              <li>
                <a class="aui-dropdown2-trigger"aria-controls="header-help-dropdown" aria-owns="header-help-dropdown"
                   aria-haspopup="true" data-container="#header .aui-header-inner" href="#header-help-dropdown">
                  <span class="aui-icon aui-icon-small aui-iconfont-help">Help</span><span class="aui-icon-dropdown"></span>
                </a>
                <nav id="header-help-dropdown" class="aui-dropdown2 aui-style-default aui-dropdown2-in-header" aria-hidden="true">
                  <div class="aui-dropdown2-section">
                    <ul>
                      <li>
                        <a href="/whats-new" id="features-link">
                          What's new
                        </a>
                      </li>
                    </ul>
                  </div>
                  <div class="aui-dropdown2-section">
                    <ul>
                      <li><a href="https://confluence.atlassian.com/display/BITBUCKET/bitbucket+Documentation+Home" target="_blank">Documentation</a></li>
                      <li><a href="https://confluence.atlassian.com/display/BITBUCKET/bitbucket+101" target="_blank">Bitbucket 101</a></li>
                      <li><a href="https://confluence.atlassian.com/display/BBKB/Bitbucket+Knowledge+Base+Home" target="_blank">Knowledge base</a></li>
                    </ul>
                  </div>
                  <div class="aui-dropdown2-section">
                    <ul>
                      <li><a href="https://answers.atlassian.com/tags/bitbucket/" target="_blank">Bitbucket on Atlassian Answers</a></li>
                      <li><a href="/support">Support</a></li>
                    </ul>
                  </div>
                </nav>
              </li>
                
                  
                
              
                <li>
                  <a class="aui-dropdown2-trigger"
                     aria-owns="user-dropdown" aria-haspopup="true" data-container="#header .aui-header-inner"
                     href="/mxxie" title="mxxie" id="user-dropdown-trigger">
                    <div class="aui-avatar aui-avatar-small">
                        <div class="aui-avatar-inner">
                            <img src="https://secure.gravatar.com/avatar/fd28904c71ae2ce3d72a2839ee61fcdc?d=https%3A%2F%2Fd3oaxc4q5k2d6q.cloudfront.net%2Fm%2Fab1188947552%2Fimg%2Fdefault_avatar%2F32%2Fuser_blue.png&amp;s=32" alt="mxxie" height="24" width="24" />
                        </div>
                    </div>
                  </a>
                  <nav id="user-dropdown" class="aui-dropdown2 aui-style-default" aria-hidden="true">
                    <div class="aui-dropdown2-section">
                      <ul>
                        <li>
                          <a href="/mxxie" id="profile-link">View profile</a>
                        </li>
                        <li>
                          <a href="/account/user/mxxie/" id="account-link">Manage account</a>
                        </li>
                        <li>
                            <a href="/account/notifications/" id="inbox-link">Inbox <span id="inbox-unread-count"></span></a>
                        </li>
                        <li>
                          <a href="/account/signout/">Log out</a>
                        </li>
                      </ul>
                    </div>
                      <div class="aui-dropdown2-section" id="account-admin-links">
                        <strong>Teams</strong>
                          <ul class="aui-list-truncate">
                          </ul>
                        </div>
                      <div class="aui-dropdown2-section">
                          <ul>
                              <li>
                                  <a href="#general-invite" class='general-invite-link'>Invite a friend</a>
                              </li>
                          </ul>
                      </div>
                      
                      <div class="aui-dropdown2-section">
                        <ul>
                          <li>
                            <a href="/account/create-team/" id="create-team-link">Create team</a>
                          </li>
                          <li>
                            <a href="/account/user/mxxie/convert-team/">Convert to team</a>
                          </li>
                        </ul>
                      </div>
                    
                  </nav>
                </li>
              
            </ul>
            
          </div>
        </div>
      </nav>
    </header>
      <header id="account-warning" role="banner"
              class="aui-message-banner warning ">
        <div class="center-content">
          <span class="aui-icon aui-icon-warning"></span>
          <span class="message">
            
          </span>
        </div>
      </header>
    
      <header id="aui-message-bar">
        
      </header>
    
    
  <header id="repo-warning" role="banner" class="aui-message-banner warning">
    <div class="center-content">
      <span class="aui-icon aui-icon-warning"></span>
      <span class="message">
      </span>
    </div>
  </header>
  <script id="repo-warning-template" type="text/html">
  




  This repository's ownership is pending transfer to <a href="/[[username]]">[[username]]</a>.
  Visit the <a href="/h0cked/ae-sna-clean/admin/transfer">transfer repository page</a> to view more details.


</script>
  <header id="repo-header" class="subhead row">
    <div class="center-content">
      <div class="repo-summary">
        <a class="repo-avatar-link" href="/h0cked/ae-sna-clean">
          <span class="repo-avatar-container size64" title="h0cked/AE-SNA-Clean">
  <img alt="h0cked/AE-SNA-Clean" src="https://d3oaxc4q5k2d6q.cloudfront.net/m/ab1188947552/img/language-avatars/python_64.png">
</span>

          
          <span class="locked" rel="tooltip" title="Private repository" data-placement="bottom"></span>
          
        </a>
        <h1><a class="repo-link" href="/h0cked/ae-sna-clean">AE-SNA-Clean</a></h1>
        <ul class="repo-metadata clearfix">
          <li>
            <a class="user" href="/h0cked">
              <span class="icon user">User icon</span>
              <span>h0cked</span>
            </a>
          </li>
          
          <li>
            <a class="fork-of" href="/h0cked/ae-sna">
              <span class="icon fork-of">Fork icon</span>
              <span>Fork of AE-SNA</span>
            </a>
          </li>
          
          
          
            <li class="social">
              <a class="follow following" id="repo-follow"
                 rel="nofollow"
                 href="/h0cked/ae-sna-clean/follow">
                <span class="icon follow"></span>
                <span class="text">Following</span>
              </a>
            </li>
          
          
        </ul>
      </div>
      <div id="repo-toolbar" class="bb-toolbar">
        
        <div class="aui-buttons">
          <a id="repo-clone-button" class="aui-button aui-style" href="https://mxxie@bitbucket.org/h0cked/ae-sna-clean.git">
            <span class="icon clone">Clone icon</span>
            <span>Clone</span>
            <span class="aui-icon-dropdown"></span>
          </a>
          <a id="fork-button" class="aui-button aui-style"
             href="/h0cked/ae-sna-clean/fork">
            <span class="icon fork">Fork icon</span>
            <span>Fork</span>
          </a>
        </div>
        <div class="aui-buttons">
          <a id="compare-button" class="aui-button aui-style"
             href="/h0cked/ae-sna-clean/compare">
            <span class="icon compare">Compare icon</span>
            <span>Compare</span>
          </a>
          <a id="pull-request-button" class="aui-button aui-style"
             href="/h0cked/ae-sna-clean/pull-request/new">
            <span class="icon pull-request">Pull request icon</span>
            <span>Pull request</span>
          </a>
        </div>
        
        
        

<div id="repo-clone-dialog" class="clone-dialog hidden">
  
<div class="clone-url">
  <div class="aui-buttons">
    <a href="https://mxxie@bitbucket.org/h0cked/ae-sna-clean.git"
       class="aui-button aui-style aui-dropdown2-trigger" aria-haspopup="true"
       aria-owns="clone-url-dropdown-header">
      <span class="dropdown-text">HTTPS</span>
    </a>
    <div id="clone-url-dropdown-header" class="aui-dropdown2 aui-style-default">
      <ul class="aui-list-truncate">
        <li>
          <a href="https://mxxie@bitbucket.org/h0cked/ae-sna-clean.git"
            
              data-command="git clone https://mxxie@bitbucket.org/h0cked/ae-sna-clean.git"
            
            class="item-link https">HTTPS
          </a>
        </li>
        <li>
          <a href="ssh://git@bitbucket.org/h0cked/ae-sna-clean.git"
            
              data-command="git clone git@bitbucket.org:h0cked/ae-sna-clean.git"
            
            class="item-link ssh">SSH
          </a>
        </li>
      </ul>
    </div>
    <input type="text" readonly="readonly" value="git clone https://mxxie@bitbucket.org/h0cked/ae-sna-clean.git">
  </div>
  
  <p>Need help cloning? Visit
     <a href="https://confluence.atlassian.com/x/cgozDQ" target="_blank">Bitbucket 101</a>.</p>
  
</div>


  
  
  

<div class="clone-in-sourcetree sourcetree-windows"
  data-https-url="https://mxxie@bitbucket.org/h0cked/ae-sna-clean.git"
  data-ssh-url="ssh://git@bitbucket.org/h0cked/ae-sna-clean.git">
  <p><button class="aui-button aui-style aui-button-primary">Clone in SourceTree</button></p>


  <p class="windows-text">
      
        <a href="http://www.sourcetreeapp.com" target="_blank">SourceTree</a>
        is a free Windows client by Atlassian for Git and Subversion.
      
  </p>
  <p class="mac-text">
      
        <a href="http://www.sourcetreeapp.com" target="_blank">SourceTree</a>
        is a free Mac client by Atlassian for Git, Mercurial, and Subversion.
      
  </p>
</div>

  
</div>

      </div>
    </div>
    <div class="clearfix"></div>
  </header>
  <nav id="repo-tabs" class="aui-navgroup aui-navgroup-horizontal aui-navgroup-horizontal-roomy">
    <div class="aui-navgroup-inner">
      <div class="aui-navgroup-primary">
        <ul class="aui-nav">
          
            <li>
              <a href="/h0cked/ae-sna-clean/overview" id="repo-overview-link">Overview</a>
            </li>
          
          
            <li class="aui-nav-selected">
              <a href="/h0cked/ae-sna-clean/src" id="repo-source-link">Source</a>
            </li>
          
          
            <li>
              <a href="/h0cked/ae-sna-clean/commits" id="repo-commits-link">
                Commits
              </a>
            </li>
          
          
            <li>
              <a href="/h0cked/ae-sna-clean/pull-requests" id="repo-pullrequests-link">
                Pull requests
                
                  
                
              </a>
            </li>
          
          
            
          
            <li id="issues-tab" class="
              
                
              
            ">
              <a href="/h0cked/ae-sna-clean/issues?status=new&amp;status=open" id="repo-issues-link">
                Issues
                
                  
                
              </a>
            </li>
            <li id="wiki-tab" class="
                
                  
                
              ">
              <a href="/h0cked/ae-sna-clean/wiki" id="repo-wiki-link">Wiki</a>
            </li>
          
            <li>
            <a href="/h0cked/ae-sna-clean/downloads" id="repo-downloads-link">
              Downloads
              
                
              
            </a>
            </li>
          
        </ul>
      </div>
      <div class="aui-navgroup-secondary">
        <ul class="aui-nav">
          
        </ul>
      </div>
    </div>
  </nav>

    <div id="content" role="main">
      
  <div id="repo-content">
    
  <div id="source-container">
    



<header id="source-path">
  
  <div class="labels labels-csv">
    
      <div class="aui-buttons">
        <button data-branches-tags-url="/api/1.0/repositories/h0cked/ae-sna-clean/branches-tags"
                class="aui-button aui-style branch-dialog-trigger" title="master">
          
            
              <span class="branch icon">Branch</span>
            
            <span class="name">master</span>
          
          <span class="aui-icon-dropdown"></span>
        </button>
      </div>
    
  </div>
  
  
    <div class="view-switcher">
      <div class="aui-buttons">
        
          <a href="/h0cked/ae-sna-clean/src/422b55ca2c2b/src/ae-sna/lda_based_classification.py?at=master"
             class="aui-button aui-style pjax-trigger" aria-pressed="true">
            Source
          </a>
          <a href="/h0cked/ae-sna-clean/diff/src/ae-sna/lda_based_classification.py?diff2=422b55ca2c2b&at=master"
             class="aui-button aui-style pjax-trigger"
             title="Diff to previous change">
            Diff
          </a>
          <a href="/h0cked/ae-sna-clean/history-node/422b55ca2c2b/src/ae-sna/lda_based_classification.py?at=master"
             class="aui-button aui-style pjax-trigger">
            History
          </a>
        
      </div>
    </div>
  
  <h1>
    <a href="/h0cked/ae-sna-clean/src/422b55ca2c2b?at=master"
       class="pjax-trigger" title="h0cked/ae-sna-clean at 422b55ca2c2b">AE-SNA-Clean</a> /
    
      
        
          
            <a href="/h0cked/ae-sna-clean/src/422b55ca2c2b/src?at=master"
               class="pjax-trigger">src</a> /
          
        
      
    
      
        
          
            <a href="/h0cked/ae-sna-clean/src/422b55ca2c2b/src/ae-sna?at=master"
               class="pjax-trigger">ae-sna</a> /
          
        
      
    
      
        
          <span>lda_based_classification.py</span>
        
      
    
  </h1>
  
    
    
  
  <div class="clearfix"></div>
</header>


  
    <div id="source-view">
      <div class="toolbar">
        <div class="primary">
          <div class="aui-buttons">
            
              <button id="file-history-trigger" class="aui-button aui-style changeset-info"
                      data-changeset="422b55ca2c2bfbca28d3b179514b1d271ce38b2c"
                      data-path="src/ae-sna/lda_based_classification.py"
                      data-current="422b55ca2c2bfbca28d3b179514b1d271ce38b2c">
                
                   

<img class="avatar avatar16" src="https://d3oaxc4q5k2d6q.cloudfront.net/m/ab1188947552/img/default_avatar/16/user_blue.png" alt="Anonymous avatar" />
<span class="changeset-hash">422b55c</span>
<time datetime="2013-04-08T22:10:53+00:00" class="timestamp"></time>
<span class="aui-icon-dropdown"></span>

                
              </button>
            
          </div>
        </div>
          <div class="secondary">
            
              <div class="aui-buttons">
                <a href="/h0cked/ae-sna-clean/annotate/422b55ca2c2bfbca28d3b179514b1d271ce38b2c/src/ae-sna/lda_based_classification.py?at=master"
                   class="aui-button aui-style pjax-trigger">Blame</a>
              </div>
            
            <div class="aui-buttons">
              
              <a href="/h0cked/ae-sna-clean/full-commit/422b55ca2c2b/src/ae-sna/lda_based_classification.py" class="aui-button aui-style"
                 title="View full commit 422b55c">Full commit</a>
              
              <a href="/h0cked/ae-sna-clean/raw/422b55ca2c2bfbca28d3b179514b1d271ce38b2c/src/ae-sna/lda_based_classification.py"
                 class="aui-button aui-style">Raw</a>
            </div>
          </div>
        <div class="clearfix"></div>
      </div>
    </div>

    
      
        
          <div class="file-source">
            <table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre><a href="#cl-1">  1</a>
<a href="#cl-2">  2</a>
<a href="#cl-3">  3</a>
<a href="#cl-4">  4</a>
<a href="#cl-5">  5</a>
<a href="#cl-6">  6</a>
<a href="#cl-7">  7</a>
<a href="#cl-8">  8</a>
<a href="#cl-9">  9</a>
<a href="#cl-10"> 10</a>
<a href="#cl-11"> 11</a>
<a href="#cl-12"> 12</a>
<a href="#cl-13"> 13</a>
<a href="#cl-14"> 14</a>
<a href="#cl-15"> 15</a>
<a href="#cl-16"> 16</a>
<a href="#cl-17"> 17</a>
<a href="#cl-18"> 18</a>
<a href="#cl-19"> 19</a>
<a href="#cl-20"> 20</a>
<a href="#cl-21"> 21</a>
<a href="#cl-22"> 22</a>
<a href="#cl-23"> 23</a>
<a href="#cl-24"> 24</a>
<a href="#cl-25"> 25</a>
<a href="#cl-26"> 26</a>
<a href="#cl-27"> 27</a>
<a href="#cl-28"> 28</a>
<a href="#cl-29"> 29</a>
<a href="#cl-30"> 30</a>
<a href="#cl-31"> 31</a>
<a href="#cl-32"> 32</a>
<a href="#cl-33"> 33</a>
<a href="#cl-34"> 34</a>
<a href="#cl-35"> 35</a>
<a href="#cl-36"> 36</a>
<a href="#cl-37"> 37</a>
<a href="#cl-38"> 38</a>
<a href="#cl-39"> 39</a>
<a href="#cl-40"> 40</a>
<a href="#cl-41"> 41</a>
<a href="#cl-42"> 42</a>
<a href="#cl-43"> 43</a>
<a href="#cl-44"> 44</a>
<a href="#cl-45"> 45</a>
<a href="#cl-46"> 46</a>
<a href="#cl-47"> 47</a>
<a href="#cl-48"> 48</a>
<a href="#cl-49"> 49</a>
<a href="#cl-50"> 50</a>
<a href="#cl-51"> 51</a>
<a href="#cl-52"> 52</a>
<a href="#cl-53"> 53</a>
<a href="#cl-54"> 54</a>
<a href="#cl-55"> 55</a>
<a href="#cl-56"> 56</a>
<a href="#cl-57"> 57</a>
<a href="#cl-58"> 58</a>
<a href="#cl-59"> 59</a>
<a href="#cl-60"> 60</a>
<a href="#cl-61"> 61</a>
<a href="#cl-62"> 62</a>
<a href="#cl-63"> 63</a>
<a href="#cl-64"> 64</a>
<a href="#cl-65"> 65</a>
<a href="#cl-66"> 66</a>
<a href="#cl-67"> 67</a>
<a href="#cl-68"> 68</a>
<a href="#cl-69"> 69</a>
<a href="#cl-70"> 70</a>
<a href="#cl-71"> 71</a>
<a href="#cl-72"> 72</a>
<a href="#cl-73"> 73</a>
<a href="#cl-74"> 74</a>
<a href="#cl-75"> 75</a>
<a href="#cl-76"> 76</a>
<a href="#cl-77"> 77</a>
<a href="#cl-78"> 78</a>
<a href="#cl-79"> 79</a>
<a href="#cl-80"> 80</a>
<a href="#cl-81"> 81</a>
<a href="#cl-82"> 82</a>
<a href="#cl-83"> 83</a>
<a href="#cl-84"> 84</a>
<a href="#cl-85"> 85</a>
<a href="#cl-86"> 86</a>
<a href="#cl-87"> 87</a>
<a href="#cl-88"> 88</a>
<a href="#cl-89"> 89</a>
<a href="#cl-90"> 90</a>
<a href="#cl-91"> 91</a>
<a href="#cl-92"> 92</a>
<a href="#cl-93"> 93</a>
<a href="#cl-94"> 94</a>
<a href="#cl-95"> 95</a>
<a href="#cl-96"> 96</a>
<a href="#cl-97"> 97</a>
<a href="#cl-98"> 98</a>
<a href="#cl-99"> 99</a>
<a href="#cl-100">100</a>
<a href="#cl-101">101</a>
<a href="#cl-102">102</a>
<a href="#cl-103">103</a>
<a href="#cl-104">104</a>
<a href="#cl-105">105</a>
<a href="#cl-106">106</a>
<a href="#cl-107">107</a>
<a href="#cl-108">108</a>
<a href="#cl-109">109</a>
<a href="#cl-110">110</a>
<a href="#cl-111">111</a>
<a href="#cl-112">112</a>
<a href="#cl-113">113</a>
<a href="#cl-114">114</a>
<a href="#cl-115">115</a>
<a href="#cl-116">116</a>
<a href="#cl-117">117</a>
<a href="#cl-118">118</a>
<a href="#cl-119">119</a>
<a href="#cl-120">120</a>
<a href="#cl-121">121</a>
<a href="#cl-122">122</a>
<a href="#cl-123">123</a>
<a href="#cl-124">124</a>
<a href="#cl-125">125</a>
<a href="#cl-126">126</a>
<a href="#cl-127">127</a>
<a href="#cl-128">128</a>
<a href="#cl-129">129</a>
<a href="#cl-130">130</a>
<a href="#cl-131">131</a>
<a href="#cl-132">132</a>
<a href="#cl-133">133</a>
<a href="#cl-134">134</a>
<a href="#cl-135">135</a>
<a href="#cl-136">136</a>
<a href="#cl-137">137</a>
<a href="#cl-138">138</a>
<a href="#cl-139">139</a>
<a href="#cl-140">140</a>
<a href="#cl-141">141</a>
<a href="#cl-142">142</a>
<a href="#cl-143">143</a>
<a href="#cl-144">144</a>
<a href="#cl-145">145</a>
<a href="#cl-146">146</a>
<a href="#cl-147">147</a>
<a href="#cl-148">148</a>
<a href="#cl-149">149</a>
<a href="#cl-150">150</a>
<a href="#cl-151">151</a>
<a href="#cl-152">152</a>
<a href="#cl-153">153</a>
<a href="#cl-154">154</a>
<a href="#cl-155">155</a>
<a href="#cl-156">156</a>
<a href="#cl-157">157</a>
<a href="#cl-158">158</a>
<a href="#cl-159">159</a>
<a href="#cl-160">160</a>
<a href="#cl-161">161</a>
<a href="#cl-162">162</a>
<a href="#cl-163">163</a>
<a href="#cl-164">164</a>
<a href="#cl-165">165</a>
<a href="#cl-166">166</a>
<a href="#cl-167">167</a>
<a href="#cl-168">168</a>
<a href="#cl-169">169</a>
<a href="#cl-170">170</a>
<a href="#cl-171">171</a>
<a href="#cl-172">172</a>
<a href="#cl-173">173</a>
<a href="#cl-174">174</a>
<a href="#cl-175">175</a>
<a href="#cl-176">176</a>
<a href="#cl-177">177</a>
<a href="#cl-178">178</a>
<a href="#cl-179">179</a>
<a href="#cl-180">180</a>
<a href="#cl-181">181</a>
<a href="#cl-182">182</a>
<a href="#cl-183">183</a>
<a href="#cl-184">184</a>
<a href="#cl-185">185</a>
<a href="#cl-186">186</a>
<a href="#cl-187">187</a>
<a href="#cl-188">188</a>
<a href="#cl-189">189</a>
<a href="#cl-190">190</a>
<a href="#cl-191">191</a>
<a href="#cl-192">192</a>
<a href="#cl-193">193</a>
<a href="#cl-194">194</a>
<a href="#cl-195">195</a>
<a href="#cl-196">196</a>
<a href="#cl-197">197</a>
<a href="#cl-198">198</a>
<a href="#cl-199">199</a>
<a href="#cl-200">200</a>
<a href="#cl-201">201</a>
<a href="#cl-202">202</a>
<a href="#cl-203">203</a>
<a href="#cl-204">204</a>
<a href="#cl-205">205</a>
<a href="#cl-206">206</a>
<a href="#cl-207">207</a>
<a href="#cl-208">208</a>
<a href="#cl-209">209</a>
<a href="#cl-210">210</a>
<a href="#cl-211">211</a>
<a href="#cl-212">212</a>
<a href="#cl-213">213</a>
<a href="#cl-214">214</a>
<a href="#cl-215">215</a>
<a href="#cl-216">216</a>
<a href="#cl-217">217</a>
<a href="#cl-218">218</a>
<a href="#cl-219">219</a>
<a href="#cl-220">220</a>
<a href="#cl-221">221</a>
<a href="#cl-222">222</a>
<a href="#cl-223">223</a>
<a href="#cl-224">224</a>
<a href="#cl-225">225</a>
<a href="#cl-226">226</a>
<a href="#cl-227">227</a>
<a href="#cl-228">228</a>
<a href="#cl-229">229</a>
<a href="#cl-230">230</a>
<a href="#cl-231">231</a>
<a href="#cl-232">232</a>
<a href="#cl-233">233</a>
<a href="#cl-234">234</a>
<a href="#cl-235">235</a>
<a href="#cl-236">236</a>
<a href="#cl-237">237</a>
<a href="#cl-238">238</a>
<a href="#cl-239">239</a>
<a href="#cl-240">240</a>
<a href="#cl-241">241</a>
<a href="#cl-242">242</a>
<a href="#cl-243">243</a>
<a href="#cl-244">244</a>
<a href="#cl-245">245</a>
<a href="#cl-246">246</a>
<a href="#cl-247">247</a>
<a href="#cl-248">248</a>
<a href="#cl-249">249</a>
<a href="#cl-250">250</a>
<a href="#cl-251">251</a>
<a href="#cl-252">252</a>
<a href="#cl-253">253</a>
<a href="#cl-254">254</a>
<a href="#cl-255">255</a>
<a href="#cl-256">256</a>
<a href="#cl-257">257</a>
<a href="#cl-258">258</a>
<a href="#cl-259">259</a>
<a href="#cl-260">260</a>
<a href="#cl-261">261</a>
<a href="#cl-262">262</a>
<a href="#cl-263">263</a>
<a href="#cl-264">264</a>
<a href="#cl-265">265</a>
<a href="#cl-266">266</a>
<a href="#cl-267">267</a>
<a href="#cl-268">268</a>
<a href="#cl-269">269</a>
<a href="#cl-270">270</a>
<a href="#cl-271">271</a>
<a href="#cl-272">272</a>
<a href="#cl-273">273</a>
<a href="#cl-274">274</a>
<a href="#cl-275">275</a>
<a href="#cl-276">276</a>
<a href="#cl-277">277</a>
<a href="#cl-278">278</a>
<a href="#cl-279">279</a>
<a href="#cl-280">280</a>
<a href="#cl-281">281</a>
<a href="#cl-282">282</a>
<a href="#cl-283">283</a>
<a href="#cl-284">284</a>
<a href="#cl-285">285</a>
<a href="#cl-286">286</a>
<a href="#cl-287">287</a>
<a href="#cl-288">288</a>
<a href="#cl-289">289</a>
<a href="#cl-290">290</a>
<a href="#cl-291">291</a>
<a href="#cl-292">292</a>
<a href="#cl-293">293</a>
<a href="#cl-294">294</a>
<a href="#cl-295">295</a>
<a href="#cl-296">296</a>
<a href="#cl-297">297</a>
<a href="#cl-298">298</a>
<a href="#cl-299">299</a>
<a href="#cl-300">300</a>
<a href="#cl-301">301</a>
<a href="#cl-302">302</a>
<a href="#cl-303">303</a>
<a href="#cl-304">304</a>
<a href="#cl-305">305</a>
<a href="#cl-306">306</a>
<a href="#cl-307">307</a>
<a href="#cl-308">308</a>
<a href="#cl-309">309</a>
<a href="#cl-310">310</a>
<a href="#cl-311">311</a>
<a href="#cl-312">312</a>
<a href="#cl-313">313</a>
<a href="#cl-314">314</a>
<a href="#cl-315">315</a>
<a href="#cl-316">316</a>
<a href="#cl-317">317</a>
<a href="#cl-318">318</a>
<a href="#cl-319">319</a>
<a href="#cl-320">320</a>
<a href="#cl-321">321</a>
<a href="#cl-322">322</a>
<a href="#cl-323">323</a>
<a href="#cl-324">324</a>
<a href="#cl-325">325</a>
<a href="#cl-326">326</a>
<a href="#cl-327">327</a>
<a href="#cl-328">328</a>
<a href="#cl-329">329</a>
<a href="#cl-330">330</a>
<a href="#cl-331">331</a>
<a href="#cl-332">332</a>
<a href="#cl-333">333</a>
<a href="#cl-334">334</a>
<a href="#cl-335">335</a>
<a href="#cl-336">336</a>
<a href="#cl-337">337</a>
<a href="#cl-338">338</a>
<a href="#cl-339">339</a>
<a href="#cl-340">340</a>
<a href="#cl-341">341</a>
<a href="#cl-342">342</a>
<a href="#cl-343">343</a>
<a href="#cl-344">344</a>
<a href="#cl-345">345</a>
<a href="#cl-346">346</a>
<a href="#cl-347">347</a>
<a href="#cl-348">348</a>
<a href="#cl-349">349</a>
<a href="#cl-350">350</a>
<a href="#cl-351">351</a>
<a href="#cl-352">352</a>
<a href="#cl-353">353</a>
<a href="#cl-354">354</a>
<a href="#cl-355">355</a>
<a href="#cl-356">356</a>
<a href="#cl-357">357</a>
<a href="#cl-358">358</a>
<a href="#cl-359">359</a>
<a href="#cl-360">360</a>
<a href="#cl-361">361</a>
<a href="#cl-362">362</a>
<a href="#cl-363">363</a>
<a href="#cl-364">364</a>
<a href="#cl-365">365</a>
<a href="#cl-366">366</a>
<a href="#cl-367">367</a>
<a href="#cl-368">368</a>
<a href="#cl-369">369</a>
<a href="#cl-370">370</a>
<a href="#cl-371">371</a>
<a href="#cl-372">372</a>
<a href="#cl-373">373</a>
<a href="#cl-374">374</a>
<a href="#cl-375">375</a>
<a href="#cl-376">376</a>
<a href="#cl-377">377</a>
<a href="#cl-378">378</a>
<a href="#cl-379">379</a>
<a href="#cl-380">380</a>
<a href="#cl-381">381</a>
<a href="#cl-382">382</a>
<a href="#cl-383">383</a>
<a href="#cl-384">384</a>
<a href="#cl-385">385</a>
<a href="#cl-386">386</a>
<a href="#cl-387">387</a>
<a href="#cl-388">388</a>
<a href="#cl-389">389</a>
<a href="#cl-390">390</a>
<a href="#cl-391">391</a>
<a href="#cl-392">392</a>
<a href="#cl-393">393</a>
<a href="#cl-394">394</a>
<a href="#cl-395">395</a>
<a href="#cl-396">396</a>
<a href="#cl-397">397</a>
<a href="#cl-398">398</a>
<a href="#cl-399">399</a>
<a href="#cl-400">400</a>
<a href="#cl-401">401</a>
<a href="#cl-402">402</a>
<a href="#cl-403">403</a>
<a href="#cl-404">404</a>
<a href="#cl-405">405</a>
<a href="#cl-406">406</a>
<a href="#cl-407">407</a>
<a href="#cl-408">408</a>
<a href="#cl-409">409</a>
<a href="#cl-410">410</a>
<a href="#cl-411">411</a>
<a href="#cl-412">412</a>
<a href="#cl-413">413</a>
<a href="#cl-414">414</a>
<a href="#cl-415">415</a>
<a href="#cl-416">416</a>
<a href="#cl-417">417</a>
<a href="#cl-418">418</a>
<a href="#cl-419">419</a>
<a href="#cl-420">420</a>
<a href="#cl-421">421</a>
<a href="#cl-422">422</a>
<a href="#cl-423">423</a>
<a href="#cl-424">424</a>
<a href="#cl-425">425</a>
<a href="#cl-426">426</a>
<a href="#cl-427">427</a>
<a href="#cl-428">428</a>
<a href="#cl-429">429</a>
<a href="#cl-430">430</a>
<a href="#cl-431">431</a>
<a href="#cl-432">432</a>
<a href="#cl-433">433</a>
<a href="#cl-434">434</a>
<a href="#cl-435">435</a>
<a href="#cl-436">436</a>
<a href="#cl-437">437</a>
<a href="#cl-438">438</a>
<a href="#cl-439">439</a>
<a href="#cl-440">440</a>
<a href="#cl-441">441</a>
<a href="#cl-442">442</a>
<a href="#cl-443">443</a>
<a href="#cl-444">444</a>
<a href="#cl-445">445</a>
<a href="#cl-446">446</a>
<a href="#cl-447">447</a>
<a href="#cl-448">448</a>
<a href="#cl-449">449</a>
<a href="#cl-450">450</a>
<a href="#cl-451">451</a>
<a href="#cl-452">452</a>
<a href="#cl-453">453</a>
<a href="#cl-454">454</a>
<a href="#cl-455">455</a>
<a href="#cl-456">456</a>
<a href="#cl-457">457</a>
<a href="#cl-458">458</a>
<a href="#cl-459">459</a>
<a href="#cl-460">460</a>
<a href="#cl-461">461</a>
<a href="#cl-462">462</a>
<a href="#cl-463">463</a>
<a href="#cl-464">464</a>
<a href="#cl-465">465</a>
<a href="#cl-466">466</a>
<a href="#cl-467">467</a>
<a href="#cl-468">468</a>
<a href="#cl-469">469</a>
<a href="#cl-470">470</a>
<a href="#cl-471">471</a>
<a href="#cl-472">472</a>
<a href="#cl-473">473</a>
<a href="#cl-474">474</a>
<a href="#cl-475">475</a>
<a href="#cl-476">476</a>
<a href="#cl-477">477</a>
<a href="#cl-478">478</a>
<a href="#cl-479">479</a>
<a href="#cl-480">480</a>
<a href="#cl-481">481</a>
<a href="#cl-482">482</a>
<a href="#cl-483">483</a>
<a href="#cl-484">484</a>
<a href="#cl-485">485</a>
<a href="#cl-486">486</a>
<a href="#cl-487">487</a>
<a href="#cl-488">488</a>
<a href="#cl-489">489</a>
<a href="#cl-490">490</a>
<a href="#cl-491">491</a>
<a href="#cl-492">492</a>
<a href="#cl-493">493</a>
<a href="#cl-494">494</a>
<a href="#cl-495">495</a>
<a href="#cl-496">496</a>
<a href="#cl-497">497</a>
<a href="#cl-498">498</a>
<a href="#cl-499">499</a>
<a href="#cl-500">500</a>
<a href="#cl-501">501</a>
<a href="#cl-502">502</a>
<a href="#cl-503">503</a>
<a href="#cl-504">504</a>
<a href="#cl-505">505</a>
<a href="#cl-506">506</a>
<a href="#cl-507">507</a>
<a href="#cl-508">508</a>
<a href="#cl-509">509</a>
<a href="#cl-510">510</a>
<a href="#cl-511">511</a>
<a href="#cl-512">512</a>
<a href="#cl-513">513</a>
<a href="#cl-514">514</a>
<a href="#cl-515">515</a>
<a href="#cl-516">516</a>
<a href="#cl-517">517</a>
<a href="#cl-518">518</a>
<a href="#cl-519">519</a>
<a href="#cl-520">520</a>
<a href="#cl-521">521</a>
<a href="#cl-522">522</a>
<a href="#cl-523">523</a>
<a href="#cl-524">524</a>
<a href="#cl-525">525</a>
<a href="#cl-526">526</a>
<a href="#cl-527">527</a>
<a href="#cl-528">528</a>
<a href="#cl-529">529</a>
<a href="#cl-530">530</a>
<a href="#cl-531">531</a>
<a href="#cl-532">532</a>
<a href="#cl-533">533</a>
<a href="#cl-534">534</a>
<a href="#cl-535">535</a>
<a href="#cl-536">536</a>
<a href="#cl-537">537</a>
<a href="#cl-538">538</a>
<a href="#cl-539">539</a>
<a href="#cl-540">540</a>
<a href="#cl-541">541</a>
<a href="#cl-542">542</a>
<a href="#cl-543">543</a>
<a href="#cl-544">544</a>
<a href="#cl-545">545</a>
<a href="#cl-546">546</a>
<a href="#cl-547">547</a>
<a href="#cl-548">548</a>
<a href="#cl-549">549</a>
<a href="#cl-550">550</a>
<a href="#cl-551">551</a>
<a href="#cl-552">552</a>
<a href="#cl-553">553</a>
<a href="#cl-554">554</a>
<a href="#cl-555">555</a>
<a href="#cl-556">556</a>
<a href="#cl-557">557</a>
<a href="#cl-558">558</a>
<a href="#cl-559">559</a>
<a href="#cl-560">560</a>
<a href="#cl-561">561</a>
<a href="#cl-562">562</a>
<a href="#cl-563">563</a>
<a href="#cl-564">564</a>
<a href="#cl-565">565</a>
<a href="#cl-566">566</a>
<a href="#cl-567">567</a>
<a href="#cl-568">568</a>
<a href="#cl-569">569</a>
<a href="#cl-570">570</a>
<a href="#cl-571">571</a>
<a href="#cl-572">572</a>
<a href="#cl-573">573</a>
<a href="#cl-574">574</a>
<a href="#cl-575">575</a>
<a href="#cl-576">576</a>
<a href="#cl-577">577</a></pre></div></td><td class="code"><div class="highlight"><pre><a name="cl-1"></a><span class="sd">&quot;&quot;&quot;</span>
<a name="cl-2"></a><span class="sd">=====================================================================</span>
<a name="cl-3"></a><span class="sd">test lda in gensim</span>
<a name="cl-4"></a><span class="sd">=====================================================================</span>
<a name="cl-5"></a><span class="sd">&quot;&quot;&quot;</span>
<a name="cl-6"></a><span class="k">print</span> <span class="n">__doc__</span>
<a name="cl-7"></a>
<a name="cl-8"></a><span class="kn">import</span> <span class="nn">re</span><span class="o">,</span> <span class="nn">os</span><span class="o">,</span> <span class="nn">csv</span><span class="o">,</span> <span class="nn">base64</span><span class="o">,</span> <span class="nn">pickle</span>
<a name="cl-9"></a>
<a name="cl-10"></a><span class="kn">from</span> <span class="nn">scipy</span> <span class="kn">import</span> <span class="n">interp</span>
<a name="cl-11"></a><span class="kn">import</span> <span class="nn">pylab</span> <span class="kn">as</span> <span class="nn">pl</span>
<a name="cl-12"></a><span class="kn">from</span> <span class="nn">sklearn.metrics</span> <span class="kn">import</span> <span class="n">roc_curve</span><span class="p">,</span> <span class="n">auc</span>
<a name="cl-13"></a>
<a name="cl-14"></a><span class="kn">from</span> <span class="nn">sklearn.cross_validation</span> <span class="kn">import</span> <span class="n">train_test_split</span>
<a name="cl-15"></a><span class="kn">from</span> <span class="nn">sklearn.grid_search</span> <span class="kn">import</span> <span class="n">GridSearchCV</span>
<a name="cl-16"></a><span class="kn">from</span> <span class="nn">sklearn.metrics</span> <span class="kn">import</span> <span class="n">precision_score</span>
<a name="cl-17"></a><span class="kn">from</span> <span class="nn">sklearn.metrics</span> <span class="kn">import</span> <span class="n">recall_score</span>
<a name="cl-18"></a><span class="kn">from</span> <span class="nn">svm.util</span> <span class="kn">import</span> <span class="o">*</span>
<a name="cl-19"></a><span class="kn">from</span> <span class="nn">svm</span> <span class="kn">import</span> <span class="n">feature_selection</span>
<a name="cl-20"></a><span class="kn">from</span> <span class="nn">svm</span> <span class="kn">import</span> <span class="n">sampling</span>
<a name="cl-21"></a><span class="kn">from</span> <span class="nn">svm</span> <span class="kn">import</span> <span class="n">scaling</span>
<a name="cl-22"></a>
<a name="cl-23"></a><span class="kn">from</span> <span class="nn">sklearn.svm</span> <span class="kn">import</span> <span class="n">SVC</span>
<a name="cl-24"></a><span class="kn">from</span> <span class="nn">gensim</span> <span class="kn">import</span> <span class="n">corpora</span><span class="p">,</span> <span class="n">models</span><span class="p">,</span> <span class="n">similarities</span>
<a name="cl-25"></a><span class="kn">import</span> <span class="nn">logging</span>
<a name="cl-26"></a><span class="kn">import</span> <span class="nn">nltk</span>
<a name="cl-27"></a>
<a name="cl-28"></a><span class="kn">from</span> <span class="nn">nltk.stem.wordnet</span> <span class="kn">import</span> <span class="n">WordNetLemmatizer</span>
<a name="cl-29"></a><span class="kn">from</span> <span class="nn">nltk.corpus</span> <span class="kn">import</span> <span class="n">wordnet</span> <span class="k">as</span> <span class="n">wn</span>
<a name="cl-30"></a>
<a name="cl-31"></a><span class="n">lda_num_topics</span> <span class="o">=</span> <span class="mi">100</span>
<a name="cl-32"></a><span class="n">lsi_num_topics</span> <span class="o">=</span> <span class="mi">100</span>
<a name="cl-33"></a><span class="n">rp_num_topics</span> <span class="o">=</span> <span class="mi">300</span>
<a name="cl-34"></a>
<a name="cl-35"></a><span class="n">wordNetLemmatizer</span> <span class="o">=</span> <span class="n">WordNetLemmatizer</span><span class="p">()</span>
<a name="cl-36"></a>
<a name="cl-37"></a><span class="n">logging</span><span class="o">.</span><span class="n">basicConfig</span><span class="p">(</span><span class="n">format</span><span class="o">=</span><span class="s">&#39;</span><span class="si">%(asctime)s</span><span class="s"> : </span><span class="si">%(levelname)s</span><span class="s"> : </span><span class="si">%(message)s</span><span class="s">&#39;</span><span class="p">,</span> <span class="n">level</span><span class="o">=</span><span class="n">logging</span><span class="o">.</span><span class="n">ERROR</span><span class="p">)</span>
<a name="cl-38"></a>
<a name="cl-39"></a><span class="n">logger</span> <span class="o">=</span> <span class="n">logging</span><span class="o">.</span><span class="n">getLogger</span><span class="p">(</span><span class="n">__name__</span><span class="p">)</span>
<a name="cl-40"></a>
<a name="cl-41"></a><span class="k">class</span> <span class="nc">Tweet</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span>
<a name="cl-42"></a>
<a name="cl-43"></a>    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">user_id</span><span class="p">,</span> <span class="n">timestamp</span><span class="p">,</span> <span class="n">created_at</span><span class="p">,</span> <span class="n">tweet_text</span><span class="p">):</span>
<a name="cl-44"></a>        <span class="sd">&#39;&#39;&#39;</span>
<a name="cl-45"></a><span class="sd">        &#39;&#39;&#39;</span>
<a name="cl-46"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">user_id</span> <span class="o">=</span> <span class="n">user_id</span>
<a name="cl-47"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">timestamp</span> <span class="o">=</span> <span class="n">timestamp</span>
<a name="cl-48"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">tweet_text</span> <span class="o">=</span> <span class="n">tweet_text</span>
<a name="cl-49"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">created_at</span> <span class="o">=</span> <span class="n">created_at</span>
<a name="cl-50"></a>
<a name="cl-51"></a><span class="k">class</span> <span class="nc">Subject</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span>
<a name="cl-52"></a>
<a name="cl-53"></a>    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">userId</span><span class="p">,</span> <span class="n">drugUseFlag</span><span class="p">,</span> <span class="n">sideEffectsFlag</span><span class="p">):</span>
<a name="cl-54"></a>        <span class="sd">&#39;&#39;&#39;</span>
<a name="cl-55"></a><span class="sd">        &#39;&#39;&#39;</span>
<a name="cl-56"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">userId</span> <span class="o">=</span> <span class="n">userId</span>
<a name="cl-57"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">drugUseFlag</span> <span class="o">=</span> <span class="n">drugUseFlag</span>
<a name="cl-58"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">sideEffectsFlag</span> <span class="o">=</span> <span class="n">sideEffectsFlag</span>
<a name="cl-59"></a>
<a name="cl-60"></a>    <span class="k">def</span> <span class="nf">__repr__</span><span class="p">(</span> <span class="bp">self</span> <span class="p">):</span>
<a name="cl-61"></a>        <span class="k">return</span> <span class="s">&quot;userId: </span><span class="si">%s</span><span class="s">; drugUseFlag: </span><span class="si">%s</span><span class="s">; sideEffectsFlag: </span><span class="si">%s</span><span class="s">;&quot;</span><span class="o">%</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">userId</span><span class="p">,</span><span class="bp">self</span><span class="o">.</span><span class="n">drugUseFlag</span><span class="p">,</span><span class="bp">self</span><span class="o">.</span><span class="n">sideEffectsFlag</span><span class="p">)</span>
<a name="cl-62"></a>
<a name="cl-63"></a>
<a name="cl-64"></a><span class="k">def</span> <span class="nf">get_subjects</span><span class="p">():</span>
<a name="cl-65"></a>    <span class="n">subjectLabels</span> <span class="o">=</span> <span class="n">csv</span><span class="o">.</span><span class="n">reader</span><span class="p">(</span><span class="nb">open</span><span class="p">(</span><span class="s">&quot;../../misc/subjectLabels.csv&quot;</span><span class="p">,</span> <span class="s">&quot;rU&quot;</span><span class="p">))</span>
<a name="cl-66"></a>
<a name="cl-67"></a>    <span class="n">subjects</span> <span class="o">=</span> <span class="p">{}</span>
<a name="cl-68"></a>    <span class="n">l</span><span class="o">=</span><span class="k">lambda</span> <span class="n">i</span><span class="p">:</span> <span class="mi">1</span> <span class="k">if</span> <span class="nb">int</span><span class="p">(</span><span class="n">i</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span> <span class="k">else</span> <span class="mi">0</span>
<a name="cl-69"></a>
<a name="cl-70"></a>    <span class="n">userIds</span> <span class="o">=</span> <span class="p">[]</span>
<a name="cl-71"></a>    <span class="k">for</span> <span class="n">row</span> <span class="ow">in</span> <span class="n">subjectLabels</span><span class="p">:</span>
<a name="cl-72"></a>        <span class="n">userId</span> <span class="o">=</span> <span class="n">row</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
<a name="cl-73"></a>        <span class="n">drugUseFlag</span> <span class="o">=</span> <span class="n">l</span><span class="p">(</span><span class="n">row</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span>
<a name="cl-74"></a>        <span class="n">sideEffectsFlag</span> <span class="o">=</span> <span class="n">l</span><span class="p">(</span><span class="n">row</span><span class="p">[</span><span class="mi">2</span><span class="p">])</span>
<a name="cl-75"></a>        <span class="n">subjects</span><span class="p">[</span><span class="n">userId</span><span class="p">]</span> <span class="o">=</span> <span class="n">Subject</span><span class="p">(</span><span class="n">userId</span><span class="p">,</span><span class="n">drugUseFlag</span><span class="p">,</span><span class="n">sideEffectsFlag</span><span class="p">)</span>
<a name="cl-76"></a>
<a name="cl-77"></a>        <span class="n">userIds</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">userId</span><span class="p">)</span>
<a name="cl-78"></a>
<a name="cl-79"></a>    <span class="k">return</span> <span class="n">userIds</span><span class="p">,</span><span class="n">subjects</span>
<a name="cl-80"></a>
<a name="cl-81"></a>
<a name="cl-82"></a>
<a name="cl-83"></a><span class="k">def</span> <span class="nf">loadstopwords</span><span class="p">():</span>
<a name="cl-84"></a>
<a name="cl-85"></a>    <span class="n">filtered_words_f</span> <span class="o">=</span> <span class="nb">open</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">abspath</span><span class="p">(</span><span class="s">&quot;../../misc/mallet-stopwords-en.txt&quot;</span><span class="p">),</span> <span class="s">&#39;r&#39;</span><span class="p">)</span>
<a name="cl-86"></a>
<a name="cl-87"></a>    <span class="n">filtered_words</span> <span class="o">=</span> <span class="p">[]</span>
<a name="cl-88"></a>    <span class="k">for</span> <span class="n">line</span> <span class="ow">in</span> <span class="n">filtered_words_f</span><span class="p">:</span>
<a name="cl-89"></a>        <span class="k">if</span> <span class="n">line</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span> <span class="o">==</span> <span class="s">&quot;&quot;</span><span class="p">:</span>
<a name="cl-90"></a>            <span class="k">continue</span>
<a name="cl-91"></a>
<a name="cl-92"></a>        <span class="n">filtered_words</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">line</span><span class="o">.</span><span class="n">strip</span><span class="p">())</span>
<a name="cl-93"></a>
<a name="cl-94"></a>    <span class="k">return</span> <span class="n">filtered_words</span>
<a name="cl-95"></a>
<a name="cl-96"></a><span class="n">reply_tag_re</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">compile</span><span class="p">(</span><span class="s">r&#39;(@.*?)\s+&#39;</span><span class="p">,</span><span class="n">re</span><span class="o">.</span><span class="n">I</span><span class="p">)</span>
<a name="cl-97"></a><span class="k">def</span> <span class="nf">strip_reply_tags</span><span class="p">(</span><span class="n">text</span><span class="p">):</span>
<a name="cl-98"></a>    <span class="k">return</span> <span class="n">reply_tag_re</span><span class="o">.</span><span class="n">sub</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\1</span><span class="s">&#39;</span><span class="p">,</span><span class="s">&#39; </span><span class="si">%s</span><span class="s"> &#39;</span><span class="o">%</span><span class="n">text</span><span class="p">)</span>
<a name="cl-99"></a>
<a name="cl-100"></a><span class="n">url_re</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">compile</span><span class="p">(</span><span class="s">r&quot;(http.*?|www\..*?|bit\.ly.*?)\s+&quot;</span><span class="p">,</span><span class="n">re</span><span class="o">.</span><span class="n">I</span><span class="p">)</span>
<a name="cl-101"></a><span class="k">def</span> <span class="nf">strip_urls</span><span class="p">(</span><span class="n">text</span><span class="p">):</span>
<a name="cl-102"></a>    <span class="k">return</span> <span class="n">url_re</span><span class="o">.</span><span class="n">sub</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\1</span><span class="s">&#39;</span><span class="p">,</span><span class="s">&#39; </span><span class="si">%s</span><span class="s"> &#39;</span><span class="o">%</span><span class="n">text</span><span class="p">)</span>
<a name="cl-103"></a>
<a name="cl-104"></a><span class="k">def</span> <span class="nf">mreplace</span><span class="p">(</span><span class="n">s</span><span class="p">,</span> <span class="n">chars</span><span class="p">,</span> <span class="n">replace_to</span> <span class="o">=</span> <span class="s">&#39;&#39;</span><span class="p">):</span>
<a name="cl-105"></a>
<a name="cl-106"></a>    <span class="k">for</span> <span class="n">char</span> <span class="ow">in</span> <span class="n">chars</span><span class="p">:</span>
<a name="cl-107"></a>        <span class="n">s</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">s</span><span class="p">)</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="n">char</span><span class="p">,</span><span class="n">replace_to</span><span class="p">)</span>
<a name="cl-108"></a>
<a name="cl-109"></a>    <span class="k">return</span> <span class="n">s</span>
<a name="cl-110"></a>
<a name="cl-111"></a><span class="c">#preprocess indiviudal tweet, such as removing the reply tag, the url, etc.</span>
<a name="cl-112"></a><span class="k">def</span> <span class="nf">preprocess_tweet</span><span class="p">(</span><span class="n">tweet</span><span class="p">):</span>
<a name="cl-113"></a>    <span class="n">tweet</span> <span class="o">=</span> <span class="n">strip_urls</span><span class="p">(</span><span class="n">strip_reply_tags</span><span class="p">(</span><span class="n">tweet</span><span class="p">))</span>
<a name="cl-114"></a>
<a name="cl-115"></a>    <span class="k">return</span> <span class="n">tweet</span><span class="o">.</span><span class="n">lower</span><span class="p">()</span>
<a name="cl-116"></a>
<a name="cl-117"></a>
<a name="cl-118"></a><span class="c">#symbols that need to be removed when appearing as part of other words</span>
<a name="cl-119"></a><span class="n">replace_symbols</span> <span class="o">=</span> <span class="p">[</span><span class="s">&#39;</span><span class="se">\x01</span><span class="s">&#39;</span><span class="p">,</span><span class="s">&#39;!&#39;</span><span class="p">,</span><span class="s">&quot;.&quot;</span><span class="p">,</span><span class="s">&quot;?&quot;</span><span class="p">,</span><span class="s">&quot;$&quot;</span><span class="p">,</span><span class="s">&quot;#&quot;</span><span class="p">,</span> <span class="s">&#39;1&#39;</span><span class="p">,</span><span class="s">&#39;2&#39;</span><span class="p">,</span><span class="s">&#39;0&#39;</span><span class="p">,</span><span class="s">&#39;3&#39;</span><span class="p">,</span><span class="s">&#39;4&#39;</span><span class="p">,</span><span class="s">&#39;5&#39;</span><span class="p">,</span><span class="s">&#39;6&#39;</span><span class="p">,</span><span class="s">&#39;7&#39;</span><span class="p">,</span><span class="s">&#39;8&#39;</span><span class="p">,</span><span class="s">&#39;9&#39;</span><span class="p">]</span>
<a name="cl-120"></a>
<a name="cl-121"></a><span class="c">#symbols that need to be removed when appearing as a word</span>
<a name="cl-122"></a><span class="n">single_letter_symbols</span> <span class="o">=</span> <span class="p">[</span><span class="s">&#39;/&#39;</span><span class="p">,</span><span class="s">&#39;</span><span class="se">\&#39;</span><span class="s">&#39;</span><span class="p">]</span>
<a name="cl-123"></a><span class="c">#single_letter_symbols.extend(replace_symbols)</span>
<a name="cl-124"></a>
<a name="cl-125"></a><span class="n">stopwords</span> <span class="o">=</span> <span class="n">loadstopwords</span><span class="p">()</span> <span class="c">#set(&#39;for a of the and to in that was is&#39;.split())</span>
<a name="cl-126"></a><span class="n">stopwords</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">nltk</span><span class="o">.</span><span class="n">corpus</span><span class="o">.</span><span class="n">stopwords</span><span class="o">.</span><span class="n">words</span><span class="p">(</span><span class="s">&#39;english&#39;</span><span class="p">))</span>
<a name="cl-127"></a>
<a name="cl-128"></a><span class="n">stopwords</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">single_letter_symbols</span><span class="p">)</span>
<a name="cl-129"></a>
<a name="cl-130"></a><span class="n">twitter_stopwords</span> <span class="o">=</span> <span class="p">[</span><span class="s">&#39;rt&#39;</span><span class="p">,</span><span class="s">&#39;i</span><span class="se">\&#39;</span><span class="s">m&#39;</span><span class="p">,</span><span class="s">&#39;it</span><span class="se">\&#39;</span><span class="s">s&#39;</span><span class="p">,</span><span class="s">&#39;that</span><span class="se">\&#39;</span><span class="s">s&#39;</span><span class="p">,</span><span class="s">&#39;don</span><span class="se">\&#39;</span><span class="s">t&#39;</span><span class="p">,</span><span class="s">&#39;i</span><span class="se">\&#39;</span><span class="s">ve&#39;</span><span class="p">,</span><span class="s">&#39;n</span><span class="se">\&#39;</span><span class="s">t&#39;</span><span class="p">,</span><span class="s">&#39;ly&#39;</span><span class="p">,</span><span class="s">&#39;</span><span class="se">\&#39;</span><span class="s">m&#39;</span><span class="p">,</span><span class="s">&#39;--&#39;</span><span class="p">,</span> <span class="s">&#39;||&#39;</span><span class="p">,</span> <span class="s">&#39;ll&#39;</span><span class="p">,</span> <span class="s">&#39;ff&#39;</span><span class="p">]</span>
<a name="cl-131"></a><span class="n">stopwords</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">twitter_stopwords</span><span class="p">)</span>
<a name="cl-132"></a>
<a name="cl-133"></a><span class="c">#Anything else with be None, and will be removed from the corpus</span>
<a name="cl-134"></a><span class="c">#morphy_tag = {&#39;NN.*&#39;:wn.NOUN,</span>
<a name="cl-135"></a><span class="c">#              &#39;JJ.*&#39;:wn.ADJ,</span>
<a name="cl-136"></a><span class="c">#              &#39;VB.*&#39;:wn.VERB,</span>
<a name="cl-137"></a><span class="c">#              &#39;RB.*&#39;:wn.ADV}</span>
<a name="cl-138"></a>
<a name="cl-139"></a><span class="n">morphy_tag</span> <span class="o">=</span> <span class="p">{</span><span class="s">&#39;NN&#39;</span><span class="p">:</span><span class="n">wn</span><span class="o">.</span><span class="n">NOUN</span><span class="p">,</span>
<a name="cl-140"></a>              <span class="s">&#39;JJ&#39;</span><span class="p">:</span><span class="n">wn</span><span class="o">.</span><span class="n">ADJ</span><span class="p">,</span>
<a name="cl-141"></a>              <span class="s">&#39;VB&#39;</span><span class="p">:</span><span class="n">wn</span><span class="o">.</span><span class="n">VERB</span><span class="p">,</span>
<a name="cl-142"></a>              <span class="s">&#39;RB&#39;</span><span class="p">:</span><span class="n">wn</span><span class="o">.</span><span class="n">ADV</span><span class="p">}</span>
<a name="cl-143"></a>
<a name="cl-144"></a><span class="n">drugs</span> <span class="o">=</span> <span class="p">[</span><span class="s">&#39;avastin&#39;</span><span class="p">,</span><span class="s">&#39;bevacizumab&#39;</span><span class="p">,</span><span class="s">&#39;melphalan&#39;</span><span class="p">,</span><span class="s">&#39;alkeran&#39;</span><span class="p">,</span><span class="s">&#39;rupatadin&#39;</span><span class="p">,</span><span class="s">&#39;rupafin&#39;</span><span class="p">,</span><span class="s">&#39;urtimed&#39;</span><span class="p">,</span><span class="s">&#39;tamoxifen&#39;</span><span class="p">,</span><span class="s">&#39;nolvadex&#39;</span><span class="p">,</span><span class="s">&#39;taxotere&#39;</span><span class="p">,</span><span class="s">&#39;docetaxel&#39;</span><span class="p">]</span>
<a name="cl-145"></a>
<a name="cl-146"></a><span class="k">def</span> <span class="nf">preprocess_and_tokenize_document</span><span class="p">(</span><span class="n">document</span><span class="p">):</span>
<a name="cl-147"></a>
<a name="cl-148"></a>    <span class="n">tokenized_document</span> <span class="o">=</span> <span class="p">[]</span>
<a name="cl-149"></a>
<a name="cl-150"></a>    <span class="c">#lancasterStemmer = nltk.LancasterStemmer()</span>
<a name="cl-151"></a>    <span class="c">#porterStemmer = nltk.PorterStemmer()</span>
<a name="cl-152"></a>
<a name="cl-153"></a>    <span class="k">for</span> <span class="n">line</span> <span class="ow">in</span> <span class="n">document</span><span class="p">:</span>
<a name="cl-154"></a>
<a name="cl-155"></a>        <span class="n">tokenized_line</span> <span class="o">=</span> <span class="n">nltk</span><span class="o">.</span><span class="n">word_tokenize</span><span class="p">(</span><span class="n">line</span><span class="p">)</span>
<a name="cl-156"></a>        <span class="n">processed_tokenized_line</span> <span class="o">=</span> <span class="p">[]</span>
<a name="cl-157"></a>
<a name="cl-158"></a>        <span class="n">tagged_line</span> <span class="o">=</span> <span class="n">nltk</span><span class="o">.</span><span class="n">pos_tag</span><span class="p">(</span><span class="n">tokenized_line</span><span class="p">)</span>
<a name="cl-159"></a>
<a name="cl-160"></a>
<a name="cl-161"></a>        <span class="k">for</span> <span class="n">w</span> <span class="ow">in</span> <span class="n">tagged_line</span><span class="p">:</span>
<a name="cl-162"></a>            <span class="n">word</span> <span class="o">=</span> <span class="n">w</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
<a name="cl-163"></a>            <span class="n">tag</span> <span class="o">=</span> <span class="n">w</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span>
<a name="cl-164"></a>            <span class="n">s_tag</span> <span class="o">=</span> <span class="n">tag</span><span class="p">[:</span><span class="mi">2</span><span class="p">]</span>
<a name="cl-165"></a>
<a name="cl-166"></a>            <span class="k">if</span> <span class="n">word</span> <span class="ow">in</span> <span class="n">drugs</span><span class="p">:</span>
<a name="cl-167"></a>                <span class="n">word</span> <span class="o">=</span> <span class="s">&#39;drug&#39;</span>
<a name="cl-168"></a>            <span class="k">else</span><span class="p">:</span>
<a name="cl-169"></a>                <span class="n">wnWord</span> <span class="o">=</span> <span class="n">wn</span><span class="o">.</span><span class="n">synsets</span><span class="p">(</span><span class="n">word</span><span class="p">)</span>
<a name="cl-170"></a>                <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">wnWord</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span> <span class="ow">and</span> <span class="n">s_tag</span> <span class="ow">in</span> <span class="n">morphy_tag</span><span class="p">:</span>
<a name="cl-171"></a>                    <span class="n">processed_tokenized_line</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">wordNetLemmatizer</span><span class="o">.</span><span class="n">lemmatize</span><span class="p">(</span><span class="n">word</span><span class="p">,</span> <span class="n">morphy_tag</span><span class="p">[</span><span class="n">s_tag</span><span class="p">]))</span>
<a name="cl-172"></a>            <span class="c">#print(w + &quot;===&quot; + wordNetLemmatizer.lemmatize(w) + &quot;===&quot; + porterStemmer.stem(w))</span>
<a name="cl-173"></a>
<a name="cl-174"></a>        <span class="n">tokenized_document</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">tokenized_line</span><span class="p">)</span>
<a name="cl-175"></a>
<a name="cl-176"></a>
<a name="cl-177"></a>    <span class="n">tokenized_document</span> <span class="o">=</span> <span class="p">[</span><span class="n">word</span> <span class="k">for</span> <span class="n">word</span> <span class="ow">in</span> <span class="p">[</span><span class="n">mreplace</span><span class="p">(</span><span class="n">word</span><span class="p">,</span> <span class="n">replace_symbols</span><span class="p">)</span> <span class="k">for</span> <span class="n">word</span> <span class="ow">in</span> <span class="n">tokenized_document</span> <span class="k">if</span> <span class="n">word</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">single_letter_symbols</span> <span class="ow">and</span> <span class="nb">len</span><span class="p">(</span><span class="n">word</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">1</span><span class="p">]</span> <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">word</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">1</span> <span class="ow">and</span> <span class="n">word</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">stopwords</span><span class="p">]</span>
<a name="cl-178"></a>
<a name="cl-179"></a>    <span class="k">return</span> <span class="n">tokenized_document</span>
<a name="cl-180"></a>
<a name="cl-181"></a>
<a name="cl-182"></a>
<a name="cl-183"></a><span class="k">def</span> <span class="nf">preprocess_tokenized_documents</span><span class="p">(</span><span class="n">tokenized_documents</span><span class="p">,</span> <span class="n">tokens_once</span> <span class="o">=</span> <span class="bp">None</span><span class="p">):</span>
<a name="cl-184"></a>
<a name="cl-185"></a>    <span class="c">#tokens_once is only collected on training set, for testing set, use the tokens_once from the training set.</span>
<a name="cl-186"></a>    <span class="k">if</span> <span class="n">tokens_once</span> <span class="o">==</span> <span class="bp">None</span><span class="p">:</span>
<a name="cl-187"></a>        <span class="n">all_tokens</span> <span class="o">=</span> <span class="nb">sum</span><span class="p">(</span><span class="n">tokenized_documents</span><span class="p">,</span> <span class="p">[])</span>
<a name="cl-188"></a>        <span class="n">tokens_once</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">word</span> <span class="k">for</span> <span class="n">word</span> <span class="ow">in</span> <span class="nb">set</span><span class="p">(</span><span class="n">all_tokens</span><span class="p">)</span> <span class="k">if</span> <span class="n">all_tokens</span><span class="o">.</span><span class="n">count</span><span class="p">(</span><span class="n">word</span><span class="p">)</span> <span class="o">==</span> <span class="mi">1</span><span class="p">)</span>
<a name="cl-189"></a>
<a name="cl-190"></a>    <span class="n">documents</span> <span class="o">=</span> <span class="p">[]</span>
<a name="cl-191"></a>    <span class="k">for</span> <span class="n">tokenized_document</span> <span class="ow">in</span> <span class="n">tokenized_documents</span><span class="p">:</span>
<a name="cl-192"></a>        <span class="c"># first, we need remove words that only appeared once...</span>
<a name="cl-193"></a>        <span class="c"># and we replace the drug name to the word drug... so that we don&#39;t really care the name of the drugs...</span>
<a name="cl-194"></a>        <span class="n">documents</span><span class="o">.</span><span class="n">append</span><span class="p">([</span><span class="n">word</span> <span class="k">for</span> <span class="n">word</span> <span class="ow">in</span> <span class="n">tokenized_document</span> <span class="k">if</span> <span class="n">word</span> <span class="ow">not</span> <span class="ow">in</span> <span class="nb">list</span><span class="p">(</span><span class="n">tokens_once</span><span class="p">)])</span>
<a name="cl-195"></a>
<a name="cl-196"></a>
<a name="cl-197"></a>    <span class="k">return</span> <span class="n">tokens_once</span><span class="p">,</span> <span class="n">documents</span>
<a name="cl-198"></a>
<a name="cl-199"></a>
<a name="cl-200"></a><span class="k">def</span> <span class="nf">load_corpus</span><span class="p">():</span>
<a name="cl-201"></a>    <span class="n">data_folder</span> <span class="o">=</span> <span class="s">&quot;../../result/twitter-user-timeline-by-drug/DRUG/&quot;</span>
<a name="cl-202"></a>
<a name="cl-203"></a>    <span class="n">input_files</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">listdir</span><span class="p">(</span><span class="n">data_folder</span><span class="p">)</span>
<a name="cl-204"></a>
<a name="cl-205"></a>    <span class="n">uIds</span><span class="p">,</span><span class="n">subjects</span> <span class="o">=</span> <span class="n">get_subjects</span><span class="p">()</span>
<a name="cl-206"></a>
<a name="cl-207"></a>    <span class="n">documents</span> <span class="o">=</span> <span class="p">[]</span>
<a name="cl-208"></a>
<a name="cl-209"></a>    <span class="n">instances</span> <span class="o">=</span> <span class="p">[]</span>
<a name="cl-210"></a>
<a name="cl-211"></a>    <span class="k">for</span> <span class="n">input_file</span> <span class="ow">in</span> <span class="n">input_files</span><span class="p">:</span>
<a name="cl-212"></a>
<a name="cl-213"></a>        <span class="k">if</span> <span class="ow">not</span> <span class="n">input_file</span><span class="o">.</span><span class="n">endswith</span><span class="p">(</span><span class="s">&#39;.txt&#39;</span><span class="p">):</span>
<a name="cl-214"></a>            <span class="k">continue</span>
<a name="cl-215"></a>
<a name="cl-216"></a>        <span class="n">m</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">match</span><span class="p">(</span><span class="s">&quot;(\d+).*?txt&quot;</span><span class="p">,</span><span class="n">input_file</span><span class="p">)</span>
<a name="cl-217"></a>
<a name="cl-218"></a>        <span class="n">userId</span> <span class="o">=</span> <span class="n">m</span><span class="o">.</span><span class="n">group</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
<a name="cl-219"></a>
<a name="cl-220"></a>        <span class="k">if</span> <span class="n">userId</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">subjects</span><span class="p">:</span>
<a name="cl-221"></a>            <span class="k">continue</span>
<a name="cl-222"></a>
<a name="cl-223"></a>        <span class="c">#subject = [userId,subjects[userId].drugUseFlag,subjects[userId].sideEffectsFlag]</span>
<a name="cl-224"></a>
<a name="cl-225"></a>        <span class="n">txt_f</span> <span class="o">=</span> <span class="nb">open</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">abspath</span><span class="p">(</span><span class="s">&quot;</span><span class="si">%s%s</span><span class="s">&quot;</span><span class="o">%</span><span class="p">(</span><span class="n">data_folder</span><span class="p">,</span><span class="n">input_file</span><span class="p">)),</span> <span class="s">&#39;r&#39;</span><span class="p">)</span>
<a name="cl-226"></a>
<a name="cl-227"></a>        <span class="c">#tweets is a document collection of tweets</span>
<a name="cl-228"></a>        <span class="n">tweets</span> <span class="o">=</span> <span class="p">[]</span>
<a name="cl-229"></a>        <span class="k">for</span> <span class="n">tweet</span> <span class="ow">in</span> <span class="n">txt_f</span><span class="p">:</span>
<a name="cl-230"></a>            <span class="k">if</span> <span class="n">tweet</span><span class="o">.</span><span class="n">rstrip</span><span class="p">()</span> <span class="o">==</span> <span class="s">&#39;&#39;</span><span class="p">:</span>
<a name="cl-231"></a>                <span class="k">continue</span>
<a name="cl-232"></a>            <span class="n">tweets</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">preprocess_tweet</span><span class="p">(</span><span class="n">tweet</span><span class="p">))</span>
<a name="cl-233"></a>
<a name="cl-234"></a>        <span class="n">document</span> <span class="o">=</span> <span class="n">preprocess_and_tokenize_document</span><span class="p">(</span><span class="n">tweets</span><span class="p">)</span>
<a name="cl-235"></a>
<a name="cl-236"></a>        <span class="n">documents</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">document</span><span class="p">)</span>
<a name="cl-237"></a>        <span class="n">instances</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">subjects</span><span class="p">[</span><span class="n">userId</span><span class="p">])</span>
<a name="cl-238"></a>
<a name="cl-239"></a>    <span class="k">return</span> <span class="n">instances</span><span class="p">,</span><span class="n">documents</span>
<a name="cl-240"></a>
<a name="cl-241"></a>
<a name="cl-242"></a><span class="c">#train the lda on D_train and generate topic distribution of each document as features</span>
<a name="cl-243"></a><span class="k">def</span> <span class="nf">getFeatureMatrixFromLDA</span><span class="p">(</span><span class="n">y_train</span><span class="p">,</span> <span class="n">y_test</span><span class="p">,</span> <span class="n">D_train</span><span class="p">,</span> <span class="n">D_test</span><span class="p">,</span> <span class="nb">all</span> <span class="o">=</span> <span class="bp">True</span><span class="p">,</span> <span class="n">mode</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span>
<a name="cl-244"></a>
<a name="cl-245"></a>    <span class="n">num_topics</span> <span class="o">=</span> <span class="mi">20</span>
<a name="cl-246"></a>
<a name="cl-247"></a>    <span class="n">D_train_corpus</span> <span class="o">=</span> <span class="bp">None</span>
<a name="cl-248"></a>    <span class="n">D_test_corpus</span> <span class="o">=</span> <span class="bp">None</span>
<a name="cl-249"></a>
<a name="cl-250"></a>    <span class="n">dictionary</span> <span class="o">=</span> <span class="bp">None</span>
<a name="cl-251"></a>    <span class="k">if</span> <span class="n">mode</span> <span class="o">!=</span> <span class="s">&quot;positive_only&quot;</span><span class="p">:</span>
<a name="cl-252"></a>        <span class="k">if</span> <span class="nb">all</span> <span class="o">==</span> <span class="bp">True</span><span class="p">:</span>
<a name="cl-253"></a>            <span class="n">All_D</span> <span class="o">=</span> <span class="p">[]</span>
<a name="cl-254"></a>            <span class="n">All_D</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">D_train</span><span class="p">)</span>
<a name="cl-255"></a>            <span class="n">All_D</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">D_test</span><span class="p">)</span>
<a name="cl-256"></a>
<a name="cl-257"></a>            <span class="n">tokens_once</span><span class="p">,</span> <span class="n">D_tokenized</span> <span class="o">=</span> <span class="n">preprocess_tokenized_documents</span><span class="p">(</span><span class="n">All_D</span><span class="p">)</span>
<a name="cl-258"></a>            <span class="n">dictionary</span> <span class="o">=</span> <span class="n">corpora</span><span class="o">.</span><span class="n">Dictionary</span><span class="p">(</span><span class="n">D_tokenized</span><span class="p">)</span>
<a name="cl-259"></a>
<a name="cl-260"></a>            <span class="n">corpus</span> <span class="o">=</span> <span class="p">[</span><span class="n">dictionary</span><span class="o">.</span><span class="n">doc2bow</span><span class="p">(</span><span class="n">document</span><span class="p">)</span> <span class="k">for</span> <span class="n">document</span> <span class="ow">in</span> <span class="n">All_D</span><span class="p">]</span>
<a name="cl-261"></a>
<a name="cl-262"></a>            <span class="n">_</span><span class="p">,</span> <span class="n">D_train_tokenized</span> <span class="o">=</span> <span class="n">preprocess_tokenized_documents</span><span class="p">(</span><span class="n">D_train</span><span class="p">,</span> <span class="n">tokens_once</span><span class="p">)</span>
<a name="cl-263"></a>            <span class="n">_</span><span class="p">,</span> <span class="n">D_test_tokenized</span> <span class="o">=</span> <span class="n">preprocess_tokenized_documents</span><span class="p">(</span><span class="n">D_test</span><span class="p">,</span> <span class="n">tokens_once</span><span class="p">)</span>
<a name="cl-264"></a>
<a name="cl-265"></a>            <span class="n">D_train_corpus</span> <span class="o">=</span> <span class="p">[</span><span class="n">dictionary</span><span class="o">.</span><span class="n">doc2bow</span><span class="p">(</span><span class="n">document</span><span class="p">)</span> <span class="k">for</span> <span class="n">document</span> <span class="ow">in</span> <span class="n">D_train_tokenized</span><span class="p">]</span>
<a name="cl-266"></a>            <span class="n">D_test_corpus</span> <span class="o">=</span> <span class="p">[</span><span class="n">dictionary</span><span class="o">.</span><span class="n">doc2bow</span><span class="p">(</span><span class="n">document</span><span class="p">)</span> <span class="k">for</span> <span class="n">document</span> <span class="ow">in</span> <span class="n">D_test_tokenized</span><span class="p">]</span>
<a name="cl-267"></a>        <span class="k">else</span><span class="p">:</span>
<a name="cl-268"></a>            <span class="n">tokens_once</span><span class="p">,</span> <span class="n">D_train_tokenized</span> <span class="o">=</span> <span class="n">preprocess_tokenized_documents</span><span class="p">(</span><span class="n">D_train</span><span class="p">)</span>
<a name="cl-269"></a>            <span class="n">_</span><span class="p">,</span> <span class="n">D_test_tokenized</span> <span class="o">=</span> <span class="n">preprocess_tokenized_documents</span><span class="p">(</span><span class="n">D_test</span><span class="p">,</span> <span class="n">tokens_once</span><span class="p">)</span>
<a name="cl-270"></a>
<a name="cl-271"></a>            <span class="n">dictionary</span> <span class="o">=</span> <span class="n">corpora</span><span class="o">.</span><span class="n">Dictionary</span><span class="p">(</span><span class="n">D_train_tokenized</span><span class="p">)</span>
<a name="cl-272"></a>
<a name="cl-273"></a>            <span class="n">D_train_corpus</span> <span class="o">=</span> <span class="n">corpus</span> <span class="o">=</span> <span class="p">[</span><span class="n">dictionary</span><span class="o">.</span><span class="n">doc2bow</span><span class="p">(</span><span class="n">document</span><span class="p">)</span> <span class="k">for</span> <span class="n">document</span> <span class="ow">in</span> <span class="n">D_train_tokenized</span><span class="p">]</span>
<a name="cl-274"></a>            <span class="n">D_test_corpus</span> <span class="o">=</span> <span class="p">[</span><span class="n">dictionary</span><span class="o">.</span><span class="n">doc2bow</span><span class="p">(</span><span class="n">document</span><span class="p">)</span> <span class="k">for</span> <span class="n">document</span> <span class="ow">in</span> <span class="n">D_test_tokenized</span><span class="p">]</span>
<a name="cl-275"></a>    <span class="k">elif</span> <span class="n">mode</span> <span class="o">==</span> <span class="s">&quot;positive_only&quot;</span><span class="p">:</span>
<a name="cl-276"></a>        <span class="k">if</span> <span class="nb">all</span> <span class="o">==</span> <span class="bp">True</span><span class="p">:</span>
<a name="cl-277"></a>            <span class="n">p_y_train</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">flatnonzero</span><span class="p">(</span><span class="n">y_train</span> <span class="o">==</span> <span class="mi">1</span><span class="p">)</span>
<a name="cl-278"></a>            <span class="n">p_y_test</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">flatnonzero</span><span class="p">(</span><span class="n">y_test</span> <span class="o">==</span> <span class="mi">1</span><span class="p">)</span>
<a name="cl-279"></a>
<a name="cl-280"></a>            <span class="n">D</span> <span class="o">=</span> <span class="p">[]</span>
<a name="cl-281"></a>            <span class="n">D</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">D_train</span><span class="p">[</span><span class="n">p_y_train</span><span class="p">])</span>
<a name="cl-282"></a>            <span class="n">D</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">D_test</span><span class="p">[</span><span class="n">p_y_test</span><span class="p">])</span>
<a name="cl-283"></a>
<a name="cl-284"></a>            <span class="n">tokens_once</span><span class="p">,</span> <span class="n">D_tokenized</span> <span class="o">=</span> <span class="n">preprocess_tokenized_documents</span><span class="p">(</span><span class="n">D</span><span class="p">)</span>
<a name="cl-285"></a>            <span class="n">dictionary</span> <span class="o">=</span> <span class="n">corpora</span><span class="o">.</span><span class="n">Dictionary</span><span class="p">(</span><span class="n">D_tokenized</span><span class="p">)</span>
<a name="cl-286"></a>
<a name="cl-287"></a>            <span class="n">corpus</span> <span class="o">=</span> <span class="p">[</span><span class="n">dictionary</span><span class="o">.</span><span class="n">doc2bow</span><span class="p">(</span><span class="n">document</span><span class="p">)</span> <span class="k">for</span> <span class="n">document</span> <span class="ow">in</span> <span class="n">D</span><span class="p">]</span>
<a name="cl-288"></a>
<a name="cl-289"></a>            <span class="n">_</span><span class="p">,</span> <span class="n">D_train_tokenized</span> <span class="o">=</span> <span class="n">preprocess_tokenized_documents</span><span class="p">(</span><span class="n">D_train</span><span class="p">,</span> <span class="n">tokens_once</span><span class="p">)</span>
<a name="cl-290"></a>            <span class="n">_</span><span class="p">,</span> <span class="n">D_test_tokenized</span> <span class="o">=</span> <span class="n">preprocess_tokenized_documents</span><span class="p">(</span><span class="n">D_test</span><span class="p">,</span> <span class="n">tokens_once</span><span class="p">)</span>
<a name="cl-291"></a>
<a name="cl-292"></a>            <span class="n">D_train_corpus</span> <span class="o">=</span> <span class="p">[</span><span class="n">dictionary</span><span class="o">.</span><span class="n">doc2bow</span><span class="p">(</span><span class="n">document</span><span class="p">)</span> <span class="k">for</span> <span class="n">document</span> <span class="ow">in</span> <span class="n">D_train_tokenized</span><span class="p">]</span>
<a name="cl-293"></a>            <span class="n">D_test_corpus</span> <span class="o">=</span> <span class="p">[</span><span class="n">dictionary</span><span class="o">.</span><span class="n">doc2bow</span><span class="p">(</span><span class="n">document</span><span class="p">)</span> <span class="k">for</span> <span class="n">document</span> <span class="ow">in</span> <span class="n">D_test_tokenized</span><span class="p">]</span>
<a name="cl-294"></a>        <span class="k">else</span><span class="p">:</span>
<a name="cl-295"></a>            <span class="n">p_y_train</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">flatnonzero</span><span class="p">(</span><span class="n">y_train</span> <span class="o">==</span> <span class="mi">1</span><span class="p">)</span>
<a name="cl-296"></a>
<a name="cl-297"></a>            <span class="n">D</span> <span class="o">=</span> <span class="n">D_train</span><span class="p">[</span><span class="n">p_y_train</span><span class="p">]</span>
<a name="cl-298"></a>
<a name="cl-299"></a>            <span class="n">tokens_once</span><span class="p">,</span> <span class="n">D_tokenized</span> <span class="o">=</span> <span class="n">preprocess_tokenized_documents</span><span class="p">(</span><span class="n">D</span><span class="p">)</span>
<a name="cl-300"></a>            <span class="n">dictionary</span> <span class="o">=</span> <span class="n">corpora</span><span class="o">.</span><span class="n">Dictionary</span><span class="p">(</span><span class="n">D_tokenized</span><span class="p">)</span>
<a name="cl-301"></a>
<a name="cl-302"></a>            <span class="n">corpus</span> <span class="o">=</span> <span class="p">[</span><span class="n">dictionary</span><span class="o">.</span><span class="n">doc2bow</span><span class="p">(</span><span class="n">document</span><span class="p">)</span> <span class="k">for</span> <span class="n">document</span> <span class="ow">in</span> <span class="n">D</span><span class="p">]</span>
<a name="cl-303"></a>
<a name="cl-304"></a>            <span class="n">_</span><span class="p">,</span> <span class="n">D_train_tokenized</span> <span class="o">=</span> <span class="n">preprocess_tokenized_documents</span><span class="p">(</span><span class="n">D_train</span><span class="p">,</span> <span class="n">tokens_once</span><span class="p">)</span>
<a name="cl-305"></a>            <span class="n">_</span><span class="p">,</span> <span class="n">D_test_tokenized</span> <span class="o">=</span> <span class="n">preprocess_tokenized_documents</span><span class="p">(</span><span class="n">D_test</span><span class="p">,</span> <span class="n">tokens_once</span><span class="p">)</span>
<a name="cl-306"></a>
<a name="cl-307"></a>            <span class="n">D_train_corpus</span> <span class="o">=</span> <span class="p">[</span><span class="n">dictionary</span><span class="o">.</span><span class="n">doc2bow</span><span class="p">(</span><span class="n">document</span><span class="p">)</span> <span class="k">for</span> <span class="n">document</span> <span class="ow">in</span> <span class="n">D_train_tokenized</span><span class="p">]</span>
<a name="cl-308"></a>            <span class="n">D_test_corpus</span> <span class="o">=</span> <span class="p">[</span><span class="n">dictionary</span><span class="o">.</span><span class="n">doc2bow</span><span class="p">(</span><span class="n">document</span><span class="p">)</span> <span class="k">for</span> <span class="n">document</span> <span class="ow">in</span> <span class="n">D_test_tokenized</span><span class="p">]</span>
<a name="cl-309"></a>
<a name="cl-310"></a>
<a name="cl-311"></a>    <span class="n">lda</span> <span class="o">=</span> <span class="n">models</span><span class="o">.</span><span class="n">ldamodel</span><span class="o">.</span><span class="n">LdaModel</span><span class="p">(</span><span class="n">corpus</span><span class="o">=</span><span class="n">corpus</span><span class="p">,</span> <span class="n">id2word</span><span class="o">=</span><span class="n">dictionary</span><span class="p">,</span> <span class="n">num_topics</span><span class="o">=</span><span class="n">num_topics</span><span class="p">,</span> <span class="n">update_every</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span> <span class="n">chunksize</span><span class="o">=</span><span class="mi">10000</span><span class="p">,</span> <span class="n">passes</span><span class="o">=</span><span class="mi">20</span><span class="p">)</span>
<a name="cl-312"></a>
<a name="cl-313"></a>    <span class="c">#lda.show_topics(topics=-1)</span>
<a name="cl-314"></a>
<a name="cl-315"></a>    <span class="n">X_train</span> <span class="o">=</span> <span class="p">[]</span>
<a name="cl-316"></a>
<a name="cl-317"></a>    <span class="k">for</span> <span class="n">vec</span> <span class="ow">in</span> <span class="n">D_train_corpus</span><span class="p">:</span>
<a name="cl-318"></a>        <span class="n">featureVector</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">zeros</span><span class="p">(</span><span class="mi">20</span><span class="p">)</span>
<a name="cl-319"></a>
<a name="cl-320"></a>        <span class="k">for</span> <span class="n">tId</span><span class="p">,</span> <span class="n">tp</span> <span class="ow">in</span> <span class="n">lda</span><span class="p">[</span><span class="n">vec</span><span class="p">]:</span>
<a name="cl-321"></a>            <span class="n">featureVector</span><span class="p">[</span><span class="n">tId</span><span class="p">]</span> <span class="o">=</span> <span class="n">tp</span>
<a name="cl-322"></a>
<a name="cl-323"></a>        <span class="n">X_train</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">featureVector</span><span class="p">)</span>
<a name="cl-324"></a>
<a name="cl-325"></a>    <span class="n">X_test</span> <span class="o">=</span> <span class="p">[]</span>
<a name="cl-326"></a>
<a name="cl-327"></a>    <span class="k">for</span> <span class="n">vec</span> <span class="ow">in</span> <span class="n">D_test_corpus</span><span class="p">:</span>
<a name="cl-328"></a>        <span class="n">featureVector</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">zeros</span><span class="p">(</span><span class="mi">20</span><span class="p">)</span>
<a name="cl-329"></a>
<a name="cl-330"></a>        <span class="k">for</span> <span class="n">tId</span><span class="p">,</span> <span class="n">tp</span> <span class="ow">in</span> <span class="n">lda</span><span class="p">[</span><span class="n">vec</span><span class="p">]:</span>
<a name="cl-331"></a>            <span class="n">featureVector</span><span class="p">[</span><span class="n">tId</span><span class="p">]</span> <span class="o">=</span> <span class="n">tp</span>
<a name="cl-332"></a>
<a name="cl-333"></a>        <span class="n">X_test</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">featureVector</span><span class="p">)</span>
<a name="cl-334"></a>
<a name="cl-335"></a>    <span class="k">return</span> <span class="n">lda</span><span class="p">,</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="n">X_train</span><span class="p">),</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="n">X_test</span><span class="p">)</span>
<a name="cl-336"></a>
<a name="cl-337"></a>
<a name="cl-338"></a><span class="c"># SVM setup</span>
<a name="cl-339"></a><span class="c"># Set the parameters by cross-validation</span>
<a name="cl-340"></a><span class="c">#tuned_parameters = [{&#39;kernel&#39;: [&#39;linear&#39;], &#39;C&#39;: [1, 10, 100, 1000, 10000]}]</span>
<a name="cl-341"></a>
<a name="cl-342"></a><span class="c"># Set the parameters by cross-validation</span>
<a name="cl-343"></a><span class="n">tuned_parameters</span> <span class="o">=</span> <span class="p">[{</span><span class="s">&#39;kernel&#39;</span><span class="p">:</span> <span class="p">[</span><span class="s">&#39;rbf&#39;</span><span class="p">],</span> <span class="s">&#39;gamma&#39;</span><span class="p">:</span> <span class="n">range_log2based</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="o">-</span><span class="mi">13</span><span class="p">,</span> <span class="o">-</span><span class="mi">2</span><span class="p">),</span>
<a name="cl-344"></a>                     <span class="s">&#39;C&#39;</span><span class="p">:</span> <span class="n">range_log2based</span><span class="p">(</span><span class="o">-</span><span class="mi">2</span><span class="p">,</span> <span class="mi">11</span><span class="p">,</span> <span class="mi">2</span><span class="p">)}]</span><span class="c">#,</span>
<a name="cl-345"></a>                    <span class="c">#{&#39;kernel&#39;: [&#39;linear&#39;], &#39;C&#39;: [1, 10, 100, 1000]}]</span>
<a name="cl-346"></a>
<a name="cl-347"></a><span class="n">scores</span> <span class="o">=</span> <span class="p">[</span>
<a name="cl-348"></a>    <span class="p">(</span><span class="s">&#39;precision&#39;</span><span class="p">,</span> <span class="n">precision_score</span><span class="p">),</span>
<a name="cl-349"></a>    <span class="p">(</span><span class="s">&#39;recall&#39;</span><span class="p">,</span> <span class="n">recall_score</span><span class="p">),</span>
<a name="cl-350"></a>    <span class="p">]</span>
<a name="cl-351"></a>
<a name="cl-352"></a><span class="n">score_name</span> <span class="o">=</span> <span class="s">&#39;recall&#39;</span>
<a name="cl-353"></a><span class="n">score_func</span> <span class="o">=</span> <span class="n">recall_score</span>
<a name="cl-354"></a>
<a name="cl-355"></a><span class="n">fselector</span> <span class="o">=</span> <span class="n">feature_selection</span><span class="o">.</span><span class="n">FeatureSelector</span><span class="p">(</span><span class="n">mode</span><span class="o">=</span><span class="s">&#39;fscore&#39;</span><span class="p">,</span> <span class="n">params</span><span class="o">=</span><span class="p">{</span><span class="s">&#39;tuned_parameters&#39;</span><span class="p">:</span> <span class="n">tuned_parameters</span><span class="p">,</span> <span class="s">&#39;min_num_of_features&#39;</span><span class="p">:</span> <span class="mi">2</span><span class="p">})</span>
<a name="cl-356"></a>
<a name="cl-357"></a><span class="n">result_folder</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">abspath</span><span class="p">(</span><span class="s">&quot;../../result/lda&quot;</span><span class="p">)</span>
<a name="cl-358"></a>
<a name="cl-359"></a><span class="k">def</span> <span class="nf">getBoWCorpus</span><span class="p">(</span><span class="n">documents</span><span class="p">):</span>
<a name="cl-360"></a>    <span class="n">dictionary</span> <span class="o">=</span> <span class="n">corpora</span><span class="o">.</span><span class="n">Dictionary</span><span class="p">(</span><span class="n">documents</span><span class="p">)</span>
<a name="cl-361"></a>    <span class="n">bow_corpus</span> <span class="o">=</span> <span class="p">[</span><span class="n">dictionary</span><span class="o">.</span><span class="n">doc2bow</span><span class="p">(</span><span class="n">document</span><span class="p">)</span> <span class="k">for</span> <span class="n">document</span> <span class="ow">in</span> <span class="n">documents</span><span class="p">]</span>
<a name="cl-362"></a>
<a name="cl-363"></a>    <span class="k">return</span> <span class="n">bow_corpus</span><span class="p">,</span> <span class="n">dictionary</span>
<a name="cl-364"></a>
<a name="cl-365"></a><span class="k">def</span> <span class="nf">extract_lda_features</span><span class="p">(</span><span class="n">bow_corpus</span><span class="p">,</span> <span class="n">dictionary</span><span class="p">):</span>
<a name="cl-366"></a>
<a name="cl-367"></a>    <span class="n">lda</span> <span class="o">=</span> <span class="n">models</span><span class="o">.</span><span class="n">ldamodel</span><span class="o">.</span><span class="n">LdaModel</span><span class="p">(</span><span class="n">corpus</span><span class="o">=</span><span class="n">bow_corpus</span><span class="p">,</span> <span class="n">id2word</span><span class="o">=</span><span class="n">dictionary</span><span class="p">,</span> <span class="n">num_topics</span><span class="o">=</span><span class="n">lda_num_topics</span><span class="p">,</span> <span class="n">update_every</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span> <span class="n">chunksize</span><span class="o">=</span><span class="mi">10000</span><span class="p">,</span> <span class="n">passes</span><span class="o">=</span><span class="mi">20</span><span class="p">)</span>
<a name="cl-368"></a>
<a name="cl-369"></a>    <span class="n">lda_corpus</span> <span class="o">=</span> <span class="n">lda</span><span class="p">[</span><span class="n">bow_corpus</span><span class="p">]</span>
<a name="cl-370"></a>
<a name="cl-371"></a>    <span class="n">X</span> <span class="o">=</span> <span class="p">[]</span>
<a name="cl-372"></a>    <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="n">lda_corpus</span><span class="p">:</span>
<a name="cl-373"></a>        <span class="n">featureVector</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">zeros</span><span class="p">(</span><span class="n">lda_num_topics</span><span class="p">)</span>
<a name="cl-374"></a>
<a name="cl-375"></a>        <span class="k">for</span> <span class="n">tId</span><span class="p">,</span> <span class="n">tp</span> <span class="ow">in</span> <span class="n">doc</span><span class="p">:</span>
<a name="cl-376"></a>            <span class="n">featureVector</span><span class="p">[</span><span class="n">tId</span><span class="p">]</span> <span class="o">=</span> <span class="n">tp</span>
<a name="cl-377"></a>
<a name="cl-378"></a>        <span class="n">X</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">featureVector</span><span class="p">)</span>
<a name="cl-379"></a>
<a name="cl-380"></a>    <span class="k">return</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="n">X</span><span class="p">)</span>
<a name="cl-381"></a>
<a name="cl-382"></a><span class="k">def</span> <span class="nf">extract_log_entropy_features</span><span class="p">(</span><span class="n">bow_corpus</span><span class="p">,</span> <span class="n">dictionary</span><span class="p">):</span>
<a name="cl-383"></a>
<a name="cl-384"></a>    <span class="n">tfidf</span> <span class="o">=</span> <span class="n">models</span><span class="o">.</span><span class="n">tfidfmodel</span><span class="o">.</span><span class="n">TfidfModel</span><span class="p">(</span><span class="n">bow_corpus</span><span class="p">,</span> <span class="n">normalize</span><span class="o">=</span><span class="bp">True</span><span class="p">)</span>
<a name="cl-385"></a>
<a name="cl-386"></a>    <span class="n">tfidf_corpus</span> <span class="o">=</span> <span class="n">tfidf</span><span class="p">[</span><span class="n">bow_corpus</span><span class="p">]</span>
<a name="cl-387"></a>
<a name="cl-388"></a>    <span class="n">logentropy</span> <span class="o">=</span> <span class="n">models</span><span class="o">.</span><span class="n">logentropy_model</span><span class="o">.</span><span class="n">LogEntropyModel</span><span class="p">(</span><span class="n">corpus</span><span class="o">=</span><span class="n">tfidf_corpus</span><span class="p">,</span><span class="n">id2word</span><span class="o">=</span><span class="n">dictionary</span><span class="p">)</span>
<a name="cl-389"></a>
<a name="cl-390"></a>    <span class="n">logentropy_corpus</span> <span class="o">=</span> <span class="n">logentropy</span><span class="p">[</span><span class="n">bow_corpus</span><span class="p">]</span>
<a name="cl-391"></a>
<a name="cl-392"></a>    <span class="n">X</span> <span class="o">=</span> <span class="p">[]</span>
<a name="cl-393"></a>
<a name="cl-394"></a>    <span class="nb">max</span> <span class="o">=</span> <span class="mi">0</span>
<a name="cl-395"></a>    <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="n">logentropy_corpus</span><span class="p">:</span>
<a name="cl-396"></a>        <span class="k">for</span> <span class="n">tId</span><span class="p">,</span> <span class="n">tp</span> <span class="ow">in</span> <span class="n">doc</span><span class="p">:</span>
<a name="cl-397"></a>            <span class="k">if</span> <span class="n">tId</span> <span class="o">&gt;</span> <span class="nb">max</span><span class="p">:</span>
<a name="cl-398"></a>                <span class="nb">max</span> <span class="o">=</span> <span class="n">tId</span>
<a name="cl-399"></a>
<a name="cl-400"></a>    <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="n">logentropy_corpus</span><span class="p">:</span>
<a name="cl-401"></a>
<a name="cl-402"></a>        <span class="n">featureVector</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">zeros</span><span class="p">(</span><span class="nb">max</span> <span class="o">+</span> <span class="mi">1</span><span class="p">)</span>
<a name="cl-403"></a>
<a name="cl-404"></a>        <span class="k">for</span> <span class="n">tId</span><span class="p">,</span> <span class="n">tp</span> <span class="ow">in</span> <span class="n">doc</span><span class="p">:</span>
<a name="cl-405"></a>            <span class="n">featureVector</span><span class="p">[</span><span class="n">tId</span><span class="p">]</span> <span class="o">=</span> <span class="n">tp</span>
<a name="cl-406"></a>
<a name="cl-407"></a>        <span class="n">X</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">featureVector</span><span class="p">)</span>
<a name="cl-408"></a>
<a name="cl-409"></a>    <span class="k">return</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="n">X</span><span class="p">)</span>
<a name="cl-410"></a>
<a name="cl-411"></a><span class="k">def</span> <span class="nf">extract_rp_features</span><span class="p">(</span><span class="n">bow_corpus</span><span class="p">,</span> <span class="n">dictionary</span><span class="p">):</span>
<a name="cl-412"></a>
<a name="cl-413"></a>    <span class="n">tfidf</span> <span class="o">=</span> <span class="n">models</span><span class="o">.</span><span class="n">tfidfmodel</span><span class="o">.</span><span class="n">TfidfModel</span><span class="p">(</span><span class="n">bow_corpus</span><span class="p">,</span> <span class="n">normalize</span><span class="o">=</span><span class="bp">True</span><span class="p">)</span>
<a name="cl-414"></a>
<a name="cl-415"></a>    <span class="n">tfidf_corpus</span> <span class="o">=</span> <span class="n">tfidf</span><span class="p">[</span><span class="n">bow_corpus</span><span class="p">]</span>
<a name="cl-416"></a>
<a name="cl-417"></a>    <span class="n">rp</span> <span class="o">=</span> <span class="n">models</span><span class="o">.</span><span class="n">rpmodel</span><span class="o">.</span><span class="n">RpModel</span><span class="p">(</span><span class="n">corpus</span><span class="o">=</span><span class="n">tfidf_corpus</span><span class="p">,</span><span class="n">id2word</span><span class="o">=</span><span class="n">dictionary</span><span class="p">,</span><span class="n">num_topics</span><span class="o">=</span><span class="n">rp_num_topics</span><span class="p">)</span>
<a name="cl-418"></a>
<a name="cl-419"></a>    <span class="n">rp_corpus</span> <span class="o">=</span> <span class="n">rp</span><span class="p">[</span><span class="n">tfidf_corpus</span><span class="p">]</span>
<a name="cl-420"></a>
<a name="cl-421"></a>    <span class="n">X</span> <span class="o">=</span> <span class="p">[]</span>
<a name="cl-422"></a>
<a name="cl-423"></a>    <span class="nb">max</span> <span class="o">=</span> <span class="mi">0</span>
<a name="cl-424"></a>    <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="n">rp_corpus</span><span class="p">:</span>
<a name="cl-425"></a>        <span class="k">for</span> <span class="n">tId</span><span class="p">,</span> <span class="n">tp</span> <span class="ow">in</span> <span class="n">doc</span><span class="p">:</span>
<a name="cl-426"></a>            <span class="k">if</span> <span class="n">tId</span> <span class="o">&gt;</span> <span class="nb">max</span><span class="p">:</span>
<a name="cl-427"></a>                <span class="nb">max</span> <span class="o">=</span> <span class="n">tId</span>
<a name="cl-428"></a>
<a name="cl-429"></a>    <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="n">rp_corpus</span><span class="p">:</span>
<a name="cl-430"></a>        <span class="n">featureVector</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">zeros</span><span class="p">(</span><span class="nb">max</span> <span class="o">+</span> <span class="mi">1</span><span class="p">)</span>
<a name="cl-431"></a>
<a name="cl-432"></a>        <span class="k">for</span> <span class="n">tId</span><span class="p">,</span> <span class="n">tp</span> <span class="ow">in</span> <span class="n">doc</span><span class="p">:</span>
<a name="cl-433"></a>            <span class="n">featureVector</span><span class="p">[</span><span class="n">tId</span><span class="p">]</span> <span class="o">=</span> <span class="n">tp</span>
<a name="cl-434"></a>
<a name="cl-435"></a>        <span class="n">X</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">featureVector</span><span class="p">)</span>
<a name="cl-436"></a>
<a name="cl-437"></a>    <span class="k">return</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="n">X</span><span class="p">)</span>
<a name="cl-438"></a>
<a name="cl-439"></a>
<a name="cl-440"></a><span class="k">def</span> <span class="nf">extract_lsi_features</span><span class="p">(</span><span class="n">bow_corpus</span><span class="p">,</span> <span class="n">dictionary</span><span class="p">):</span>
<a name="cl-441"></a>    <span class="n">tfidf</span> <span class="o">=</span> <span class="n">models</span><span class="o">.</span><span class="n">tfidfmodel</span><span class="o">.</span><span class="n">TfidfModel</span><span class="p">(</span><span class="n">bow_corpus</span><span class="p">,</span> <span class="n">normalize</span><span class="o">=</span><span class="bp">True</span><span class="p">)</span>
<a name="cl-442"></a>
<a name="cl-443"></a>    <span class="n">tfidf_corpus</span> <span class="o">=</span> <span class="n">tfidf</span><span class="p">[</span><span class="n">bow_corpus</span><span class="p">]</span>
<a name="cl-444"></a>
<a name="cl-445"></a>    <span class="n">lsi</span> <span class="o">=</span> <span class="n">models</span><span class="o">.</span><span class="n">LsiModel</span><span class="p">(</span><span class="n">tfidf_corpus</span><span class="p">,</span> <span class="n">id2word</span><span class="o">=</span><span class="n">dictionary</span><span class="p">,</span> <span class="n">num_topics</span><span class="o">=</span><span class="n">lsi_num_topics</span><span class="p">)</span>
<a name="cl-446"></a>
<a name="cl-447"></a>    <span class="n">lsi_corpus</span> <span class="o">=</span> <span class="n">lsi</span><span class="p">[</span><span class="n">tfidf_corpus</span><span class="p">]</span>
<a name="cl-448"></a>
<a name="cl-449"></a>    <span class="n">X</span> <span class="o">=</span> <span class="p">[]</span>
<a name="cl-450"></a>    <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="n">lsi_corpus</span><span class="p">:</span>
<a name="cl-451"></a>
<a name="cl-452"></a>        <span class="n">featureVector</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">zeros</span><span class="p">(</span><span class="n">lda_num_topics</span><span class="p">)</span>
<a name="cl-453"></a>
<a name="cl-454"></a>        <span class="k">for</span> <span class="n">tId</span><span class="p">,</span> <span class="n">tp</span> <span class="ow">in</span> <span class="n">doc</span><span class="p">:</span>
<a name="cl-455"></a>            <span class="n">featureVector</span><span class="p">[</span><span class="n">tId</span><span class="p">]</span> <span class="o">=</span> <span class="n">tp</span>
<a name="cl-456"></a>
<a name="cl-457"></a>        <span class="n">X</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">featureVector</span><span class="p">)</span>
<a name="cl-458"></a>
<a name="cl-459"></a>    <span class="k">return</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="n">X</span><span class="p">)</span>
<a name="cl-460"></a>
<a name="cl-461"></a>
<a name="cl-462"></a><span class="k">def</span> <span class="nf">main</span><span class="p">():</span>
<a name="cl-463"></a>    <span class="n">n_bootstraps</span> <span class="o">=</span> <span class="mi">100</span>
<a name="cl-464"></a>
<a name="cl-465"></a>    <span class="n">instances</span><span class="p">,</span><span class="n">documents</span> <span class="o">=</span> <span class="n">load_corpus</span><span class="p">()</span>
<a name="cl-466"></a>
<a name="cl-467"></a>    <span class="n">y_o</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">([</span><span class="n">subject</span><span class="o">.</span><span class="n">drugUseFlag</span> <span class="k">for</span> <span class="n">subject</span> <span class="ow">in</span> <span class="n">instances</span><span class="p">])</span>
<a name="cl-468"></a>
<a name="cl-469"></a>    <span class="n">bow_corpus</span><span class="p">,</span> <span class="n">dictionary</span> <span class="o">=</span> <span class="n">getBoWCorpus</span><span class="p">(</span><span class="n">documents</span><span class="p">)</span>
<a name="cl-470"></a>
<a name="cl-471"></a>    <span class="n">X_rp</span> <span class="o">=</span> <span class="n">extract_rp_features</span><span class="p">(</span><span class="n">bow_corpus</span><span class="p">,</span> <span class="n">dictionary</span><span class="p">)</span>
<a name="cl-472"></a>    <span class="n">X_lda</span> <span class="o">=</span> <span class="n">extract_lda_features</span><span class="p">(</span><span class="n">bow_corpus</span><span class="p">,</span> <span class="n">dictionary</span><span class="p">)</span>
<a name="cl-473"></a>    <span class="n">X_log_entropy</span> <span class="o">=</span> <span class="n">extract_log_entropy_features</span><span class="p">(</span><span class="n">bow_corpus</span><span class="p">,</span> <span class="n">dictionary</span><span class="p">)</span>
<a name="cl-474"></a>    <span class="n">X_lsi</span> <span class="o">=</span> <span class="n">extract_lsi_features</span><span class="p">(</span><span class="n">bow_corpus</span><span class="p">,</span> <span class="n">dictionary</span><span class="p">)</span>
<a name="cl-475"></a>
<a name="cl-476"></a>    <span class="n">X_raw</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">X_rp</span><span class="p">,</span> <span class="n">X_log_entropy</span><span class="p">,</span> <span class="n">axis</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
<a name="cl-477"></a>    <span class="n">X_raw</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">X_raw</span><span class="p">,</span> <span class="n">X_lda</span><span class="p">,</span> <span class="n">axis</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
<a name="cl-478"></a>    <span class="n">X_raw</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">X_raw</span><span class="p">,</span> <span class="n">X_lsi</span><span class="p">,</span> <span class="n">axis</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
<a name="cl-479"></a>    <span class="c"># get rid of features that are zero-vectors</span>
<a name="cl-480"></a>    <span class="n">X_o</span> <span class="o">=</span> <span class="p">[]</span>
<a name="cl-481"></a>
<a name="cl-482"></a>    <span class="n">index_mapping</span> <span class="o">=</span> <span class="p">{}</span>
<a name="cl-483"></a>    <span class="n">cnt</span> <span class="o">=</span> <span class="mi">0</span>
<a name="cl-484"></a>    <span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">x</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">X_raw</span><span class="o">.</span><span class="n">transpose</span><span class="p">()):</span>
<a name="cl-485"></a>        <span class="n">zeros</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">zeros</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">x</span><span class="p">))</span>
<a name="cl-486"></a>        <span class="k">if</span> <span class="ow">not</span> <span class="n">np</span><span class="o">.</span><span class="n">array_equal</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">zeros</span><span class="p">):</span>
<a name="cl-487"></a>            <span class="n">X_o</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">x</span><span class="p">)</span>
<a name="cl-488"></a>            <span class="n">index_mapping</span><span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="o">=</span> <span class="n">cnt</span>
<a name="cl-489"></a>        <span class="n">cnt</span> <span class="o">+=</span> <span class="mi">1</span>
<a name="cl-490"></a>
<a name="cl-491"></a>    <span class="n">X_o</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="n">X_o</span><span class="p">)</span><span class="o">.</span><span class="n">transpose</span><span class="p">()</span>
<a name="cl-492"></a>    <span class="n">scaler</span> <span class="o">=</span> <span class="n">scaling</span><span class="o">.</span><span class="n">Scaler</span><span class="p">()</span>
<a name="cl-493"></a>    <span class="n">scaler</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">X_o</span><span class="p">)</span>
<a name="cl-494"></a>
<a name="cl-495"></a>    <span class="n">X_o</span> <span class="o">=</span> <span class="n">scaler</span><span class="o">.</span><span class="n">transform</span><span class="p">(</span><span class="n">X_o</span><span class="p">)</span>
<a name="cl-496"></a>
<a name="cl-497"></a>
<a name="cl-498"></a>    <span class="n">downSampling</span> <span class="o">=</span> <span class="n">sampling</span><span class="o">.</span><span class="n">BalancedDownSampling</span><span class="p">(</span><span class="n">y_o</span><span class="p">,</span> <span class="n">n_bootstraps</span><span class="o">=</span><span class="n">n_bootstraps</span><span class="p">,</span> <span class="n">random_state</span><span class="o">=</span><span class="bp">None</span><span class="p">)</span>
<a name="cl-499"></a>
<a name="cl-500"></a>    <span class="n">mean_tpr</span> <span class="o">=</span> <span class="mf">0.0</span>
<a name="cl-501"></a>    <span class="n">mean_fpr</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">linspace</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">100</span><span class="p">)</span>
<a name="cl-502"></a>    <span class="n">all_tpr</span> <span class="o">=</span> <span class="p">[]</span>
<a name="cl-503"></a>    <span class="n">all_acc</span> <span class="o">=</span> <span class="p">[]</span>
<a name="cl-504"></a>
<a name="cl-505"></a>    <span class="n">result</span> <span class="o">=</span> <span class="p">{}</span>
<a name="cl-506"></a>
<a name="cl-507"></a>    <span class="n">cnt</span> <span class="o">=</span> <span class="mi">0</span>
<a name="cl-508"></a>
<a name="cl-509"></a>    <span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">sample_indices</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">downSampling</span><span class="p">):</span>
<a name="cl-510"></a>
<a name="cl-511"></a>        <span class="n">y</span> <span class="o">=</span> <span class="n">y_o</span><span class="p">[</span><span class="n">sample_indices</span><span class="p">]</span>
<a name="cl-512"></a>        <span class="n">X</span> <span class="o">=</span> <span class="n">X_o</span><span class="p">[</span><span class="n">sample_indices</span><span class="p">]</span>
<a name="cl-513"></a>
<a name="cl-514"></a>        <span class="n">X_train</span><span class="p">,</span> <span class="n">X_test</span><span class="p">,</span> <span class="n">y_train</span><span class="p">,</span> <span class="n">y_test</span> <span class="o">=</span> <span class="n">train_test_split</span><span class="p">(</span><span class="n">X</span><span class="p">,</span> <span class="n">y</span><span class="p">,</span> <span class="n">test_size</span><span class="o">=</span><span class="mf">1.0</span><span class="o">/</span><span class="mf">10.0</span><span class="p">,</span> <span class="n">random_state</span><span class="o">=</span><span class="mi">0</span><span class="p">)</span>
<a name="cl-515"></a>
<a name="cl-516"></a>        <span class="n">fselected</span> <span class="o">=</span> <span class="n">fselector</span><span class="o">.</span><span class="n">select</span><span class="p">(</span><span class="n">X_train</span><span class="p">,</span> <span class="n">y_train</span><span class="p">)</span>
<a name="cl-517"></a>
<a name="cl-518"></a>        <span class="k">print</span><span class="p">(</span><span class="n">fselected</span><span class="p">)</span>
<a name="cl-519"></a>
<a name="cl-520"></a>        <span class="n">X_train</span> <span class="o">=</span> <span class="n">X_train</span><span class="p">[:,</span> <span class="n">fselected</span><span class="o">.</span><span class="n">best_features</span><span class="p">]</span>
<a name="cl-521"></a>        <span class="n">X_test</span> <span class="o">=</span> <span class="n">X_test</span><span class="p">[:,</span> <span class="n">fselected</span><span class="o">.</span><span class="n">best_features</span><span class="p">]</span>
<a name="cl-522"></a>
<a name="cl-523"></a>        <span class="k">print</span><span class="p">(</span><span class="s">&quot;# Tuning hyper-parameters for </span><span class="si">%s</span><span class="s">&quot;</span> <span class="o">%</span> <span class="n">score_name</span><span class="p">)</span>
<a name="cl-524"></a>
<a name="cl-525"></a>        <span class="n">clf</span> <span class="o">=</span> <span class="n">GridSearchCV</span><span class="p">(</span><span class="n">SVC</span><span class="p">(</span><span class="n">C</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span> <span class="n">probability</span><span class="o">=</span><span class="bp">True</span><span class="p">),</span> <span class="n">tuned_parameters</span><span class="p">,</span> <span class="n">score_func</span><span class="o">=</span><span class="n">score_func</span><span class="p">)</span>
<a name="cl-526"></a>        <span class="n">clf</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">X_train</span><span class="p">,</span> <span class="n">y_train</span><span class="p">,</span> <span class="n">cv</span><span class="o">=</span><span class="mi">5</span><span class="p">)</span>
<a name="cl-527"></a>
<a name="cl-528"></a>        <span class="k">print</span><span class="p">(</span><span class="s">&quot;Best parameters set found on development set: </span><span class="si">%s</span><span class="s">&quot;</span> <span class="o">%</span> <span class="n">clf</span><span class="o">.</span><span class="n">best_estimator_</span><span class="p">)</span>
<a name="cl-529"></a>        <span class="k">print</span><span class="p">(</span><span class="s">&quot;==========&quot;</span><span class="p">)</span>
<a name="cl-530"></a>
<a name="cl-531"></a>        <span class="n">clf</span> <span class="o">=</span> <span class="n">clf</span><span class="o">.</span><span class="n">best_estimator_</span>
<a name="cl-532"></a>
<a name="cl-533"></a>        <span class="n">y_true</span><span class="p">,</span> <span class="n">y_pred</span> <span class="o">=</span> <span class="n">y_test</span><span class="p">,</span> <span class="n">clf</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span><span class="n">X_test</span><span class="p">)</span>
<a name="cl-534"></a>
<a name="cl-535"></a>        <span class="n">probas_</span> <span class="o">=</span> <span class="n">clf</span><span class="o">.</span><span class="n">predict_proba</span><span class="p">(</span><span class="n">X_test</span><span class="p">)</span>
<a name="cl-536"></a>
<a name="cl-537"></a>        <span class="n">acc</span> <span class="o">=</span> <span class="n">accuracy</span><span class="p">(</span><span class="n">y_test</span><span class="p">,</span> <span class="n">y_pred</span><span class="p">)</span>
<a name="cl-538"></a>        <span class="k">print</span><span class="p">(</span><span class="s">&quot;Accuracy: </span><span class="si">%s</span><span class="s">&quot;</span><span class="p">,</span> <span class="n">acc</span><span class="p">)</span>
<a name="cl-539"></a>        <span class="n">all_acc</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">acc</span><span class="p">)</span>
<a name="cl-540"></a>
<a name="cl-541"></a>        <span class="n">fpr</span><span class="p">,</span> <span class="n">tpr</span><span class="p">,</span> <span class="n">thresholds</span> <span class="o">=</span> <span class="n">roc_curve</span><span class="p">(</span><span class="n">y_test</span><span class="p">,</span> <span class="n">probas_</span><span class="p">[:,</span> <span class="mi">1</span><span class="p">])</span>
<a name="cl-542"></a>        <span class="n">mean_tpr</span> <span class="o">+=</span> <span class="n">interp</span><span class="p">(</span><span class="n">mean_fpr</span><span class="p">,</span> <span class="n">fpr</span><span class="p">,</span> <span class="n">tpr</span><span class="p">)</span>
<a name="cl-543"></a>        <span class="n">mean_tpr</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">=</span> <span class="mf">0.0</span>
<a name="cl-544"></a>        <span class="n">roc_auc</span> <span class="o">=</span> <span class="n">auc</span><span class="p">(</span><span class="n">fpr</span><span class="p">,</span> <span class="n">tpr</span><span class="p">)</span>
<a name="cl-545"></a>        <span class="k">print</span><span class="p">(</span><span class="s">&quot;ROC_AUC: </span><span class="si">%s</span><span class="s">&quot;</span><span class="p">,</span> <span class="n">roc_auc</span><span class="p">)</span>
<a name="cl-546"></a>
<a name="cl-547"></a>
<a name="cl-548"></a>        <span class="n">cnt</span> <span class="o">+=</span> <span class="mi">1</span>
<a name="cl-549"></a>
<a name="cl-550"></a>    <span class="n">pl</span><span class="o">.</span><span class="n">plot</span><span class="p">([</span><span class="mi">0</span><span class="p">,</span> <span class="mi">1</span><span class="p">],</span> <span class="p">[</span><span class="mi">0</span><span class="p">,</span> <span class="mi">1</span><span class="p">],</span> <span class="s">&#39;--&#39;</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="p">(</span><span class="mf">0.6</span><span class="p">,</span> <span class="mf">0.6</span><span class="p">,</span> <span class="mf">0.6</span><span class="p">),</span> <span class="n">label</span><span class="o">=</span><span class="s">&#39;Luck&#39;</span><span class="p">)</span>
<a name="cl-551"></a>
<a name="cl-552"></a>    <span class="n">mean_acc</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">sum</span><span class="p">(</span><span class="n">all_acc</span><span class="p">)</span> <span class="o">/</span> <span class="n">cnt</span>
<a name="cl-553"></a>
<a name="cl-554"></a>
<a name="cl-555"></a>
<a name="cl-556"></a>    <span class="k">print</span><span class="p">(</span><span class="s">&#39;(Mean ACC: </span><span class="si">%0.2f</span><span class="s">)&#39;</span> <span class="o">%</span> <span class="n">mean_acc</span><span class="p">)</span>
<a name="cl-557"></a>    <span class="n">mean_tpr</span> <span class="o">/=</span> <span class="n">n_bootstraps</span>
<a name="cl-558"></a>    <span class="n">mean_tpr</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span> <span class="o">=</span> <span class="mf">1.0</span>
<a name="cl-559"></a>    <span class="n">mean_auc</span> <span class="o">=</span> <span class="n">auc</span><span class="p">(</span><span class="n">mean_fpr</span><span class="p">,</span> <span class="n">mean_tpr</span><span class="p">)</span>
<a name="cl-560"></a>    <span class="n">pl</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">mean_fpr</span><span class="p">,</span> <span class="n">mean_tpr</span><span class="p">,</span> <span class="s">&#39;k--&#39;</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s">&#39;red&#39;</span><span class="p">,</span>
<a name="cl-561"></a>        <span class="n">label</span><span class="o">=</span><span class="s">&#39;Mean ROC (area = </span><span class="si">%0.2f</span><span class="s">)&#39;</span> <span class="o">%</span> <span class="n">mean_auc</span><span class="p">,</span> <span class="n">lw</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span>
<a name="cl-562"></a>
<a name="cl-563"></a>    <span class="c">#plt.text(0.8, .5, &#39; Mean ACC: %0.2.f&#39; % mean_acc)</span>
<a name="cl-564"></a>    <span class="n">pl</span><span class="o">.</span><span class="n">xlim</span><span class="p">([</span><span class="o">-</span><span class="mf">0.05</span><span class="p">,</span> <span class="mf">1.05</span><span class="p">])</span>
<a name="cl-565"></a>    <span class="n">pl</span><span class="o">.</span><span class="n">ylim</span><span class="p">([</span><span class="o">-</span><span class="mf">0.05</span><span class="p">,</span> <span class="mf">1.05</span><span class="p">])</span>
<a name="cl-566"></a>    <span class="n">pl</span><span class="o">.</span><span class="n">xlabel</span><span class="p">(</span><span class="s">&#39;False Positive Rate (FTR)&#39;</span><span class="p">)</span>
<a name="cl-567"></a>    <span class="n">pl</span><span class="o">.</span><span class="n">ylabel</span><span class="p">(</span><span class="s">&#39;True Positive Rate (TPR)&#39;</span><span class="p">)</span>
<a name="cl-568"></a>    <span class="n">pl</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s">&#39;(Mean ACC: </span><span class="si">%0.2f</span><span class="s">)&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">mean_acc</span><span class="p">))</span>
<a name="cl-569"></a>    <span class="n">pl</span><span class="o">.</span><span class="n">legend</span><span class="p">(</span><span class="n">loc</span><span class="o">=</span><span class="s">&quot;lower right&quot;</span><span class="p">)</span>
<a name="cl-570"></a>
<a name="cl-571"></a>    <span class="n">pl</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
<a name="cl-572"></a>
<a name="cl-573"></a>    <span class="k">return</span>
<a name="cl-574"></a>
<a name="cl-575"></a>
<a name="cl-576"></a><span class="k">if</span> <span class="n">__name__</span> <span class="o">==</span> <span class="s">&#39;__main__&#39;</span><span class="p">:</span>
<a name="cl-577"></a>    <span class="n">main</span><span class="p">()</span>
</pre></div>
</td></tr></table>
          </div>
        
      
    
  


  <script id="source-changeset" type="text/html">
  

<a href="/h0cked/ae-sna-clean/src/[[raw_node]]/src/ae-sna/lda_based_classification.py?at=master"
   class="[[#selected]]highlight[[/selected]]"
   data-hash="[[node]]">
  [[#author.username]]
    <img class="avatar avatar16" src="[[author.avatar]]"/>
    <span class="author" title="[[raw_author]]">[[author.display_name]]</span>
  [[/author.username]]
  [[^author.username]]
    <img class="avatar avatar16" src="https://d3oaxc4q5k2d6q.cloudfront.net/m/ab1188947552/img/default_avatar/16/user_blue.png"/>
    <span class="author unmapped" title="[[raw_author]]">[[author]]</span>
  [[/author.username]]
  <time datetime="[[utctimestamp]]" data-title="true">[[utctimestamp]]</time>
  <span class="message">[[message]]</span>
</a>

</script>
  <script id="embed-template" type="text/html">
  

<form class="aui embed">
  <label for="embed-code">Embed this source in another page:</label>
  <input type="text" readonly="true" value="&lt;script src=&quot;[[url]]&quot;&gt;&lt;/script&gt;" id="embed-code">
</form>

</script>


<div class="mask"></div>



  <script id="branch-dialog-template" type="text/html">
  

<div class="tabbed-filter-widget branch-dialog">
  <div class="tabbed-filter">
    <input placeholder="Filter branches" class="filter-box" autosave="branch-dropdown-2434744" type="text">
    [[^ignoreTags]]
      <div class="aui-tabs horizontal-tabs aui-tabs-disabled filter-tabs">
        <ul class="tabs-menu">
          <li class="menu-item active-tab"><a href="#branches">Branches</a></li>
          <li class="menu-item"><a href="#tags">Tags</a></li>
        </ul>
      </div>
    [[/ignoreTags]]
  </div>
  
    <div class="tab-pane active-pane" id="branches" data-filter-placeholder="Filter branches">
      <ol class="filter-list">
        <li class="empty-msg">No matching branches</li>
        [[#branches]]
          
            [[#hasMultipleHeads]]
              [[#heads]]
                <li class="comprev filter-item">
                  <a href="/h0cked/ae-sna-clean/src/[[changeset]]/src/ae-sna/lda_based_classification.py?at=[[safeName]]"
                     title="[[name]]">
                    [[name]] ([[shortChangeset]])
                  </a>
                </li>
              [[/heads]]
            [[/hasMultipleHeads]]
            [[^hasMultipleHeads]]
              <li class="comprev filter-item">
                <a href="/h0cked/ae-sna-clean/src/[[changeset]]/src/ae-sna/lda_based_classification.py?at=[[safeName]]" title="[[name]]">
                  [[name]]
                </a>
              </li>
            [[/hasMultipleHeads]]
          
        [[/branches]]
      </ol>
    </div>
    <div class="tab-pane" id="tags" data-filter-placeholder="Filter tags">
      <ol class="filter-list">
        <li class="empty-msg">No matching tags</li>
        [[#tags]]
          <li class="comprev filter-item">
            <a href="/h0cked/ae-sna-clean/src/[[changeset]]/src/ae-sna/lda_based_classification.py?at=[[safeName]]" title="[[name]]">
              [[name]]
            </a>
          </li>
        [[/tags]]
      </ol>
    </div>
  
</div>

</script>



  </div>

  </div>
  

<form id="file-search-form" action="#"
  
  data-revision="422b55ca2c2bfbca28d3b179514b1d271ce38b2c"
  data-branch="master">
  <input type="text" id="file-search-query" class="loading">
  <div id="filtered-files"></div>
  <div class="tip"><em>Tip:</em> Filter by directory path e.g. <strong>/media app.js</strong> to search for public<strong>/media/app.js</strong>.</div>
  <div class="tip"><em>Tip:</em> Use camelCasing e.g. <strong>ProjME</strong> to search for <strong>ProjectModifiedE</strong>vent.java.</div>
  <div class="tip"><em>Tip:</em> Filter by extension type e.g. <strong>/repo .js</strong> to search for all <strong>.js</strong> files in the <strong>/repo</strong> directory.</div>
  <div class="tip"><em>Tip:</em> Separate your search with spaces e.g. <strong>/ssh pom.xml</strong> to search for src<strong>/ssh/pom.xml</strong>.</div>
  <div class="tip"><em>Tip:</em> Use ↑ and ↓ arrow keys to navigate and <strong>return</strong> to view the file.</div>
  <div class="tip mod-osx"><em>Tip:</em> You can also navigate files with <strong>Ctrl+j</strong> <em>(next)</em> and <strong>Ctrl+k</strong> <em>(previous)</em> and view the file with <strong>Ctrl+o</strong>.</div>
  <div class="tip mod-win"><em>Tip:</em> You can also navigate files with <strong>Alt+j</strong> <em>(next)</em> and <strong>Alt+k</strong> <em>(previous)</em> and view the file with <strong>Alt+o</strong>.</div>
  <script id="filtered-files-template" type="text/html">
  

<table class="aui bb-list">
  <thead>
    <tr class="assistive">
      <th class="name">Filename</th>
    </tr>
  </thead>
  <tbody>
    [[#files]]
    <tr class="iterable-item">
      <td class="name [[#isDirectory]]directory[[/isDirectory]]">
        <a href="/h0cked/ae-sna-clean/src/[[node]]/[[name]][[#branch]]?at=[[branch]][[/branch]]"
           title="[[name]]" class="execute" tabindex="-1">
          [[&highlightedName]]
        </a>
      </td>
    </tr>
    [[/files]]
  </tbody>
</table>

</script>
</form>


    </div>
  </div>
  <footer id="footer" role="contentinfo">
    <section class="footer-body">
      <ul>
        <li><a href="http://blog.bitbucket.org">Blog</a></li>
        <li><a href="//bitbucket.org/site/master/issues/new">Report a bug</a></li>
        <li><a href="/support">Support</a></li>
        <li><a href="http://confluence.atlassian.com/display/BITBUCKET">Documentation</a></li>
        <li><a href="http://confluence.atlassian.com/x/IYBGDQ">API</a></li>
        <li><a href="http://groups.google.com/group/bitbucket-users">Forum</a></li>
        <li><a href="http://status.bitbucket.org/">Server status</a></li>
        <li><a href="http://www.atlassian.com/hosted/terms.jsp">Terms of service</a></li>
        <li><a href="http://www.atlassian.com/about/privacy.jsp">Privacy policy</a></li>
      </ul>
      <ul>
        
          
            <li><a href="/account/user/mxxie/"
                   class="view-language-link">English</a></li>
          
        
        <li><a href="http://git-scm.com/">Git 1.7.10.3</a></li>
        <li><a href="http://mercurial.selenic.com/">Mercurial 2.2.2</a></li>
        <li><a href="https://www.djangoproject.com/">Django 1.3.7</a></li>
        <li><a href="http://www.python.org/">Python 2.7.3</a></li>
        <li><a href="#">5e3c22dc674c / ab1188947552 @ bitbucket01</a></li>
      </ul>
      <ul>
        <li><a href="http://www.atlassian.com?utm=bitbucket_footer">Atlassian</a></li>
        <li><a href="http://www.atlassian.com/git">Our other git tools</a></li>
      </ul>
    </section>
  </footer>
  
</div>

<script type="text/javascript" src="https://d3oaxc4q5k2d6q.cloudfront.net/m/ab1188947552/compressed/js/12c332c52f94.js"></script>

<!-- This script exists purely for the benefit of our selenium tests -->
<script>
  setTimeout(function () {
    BB.JsLoaded = true;
  }, 3000);
</script>



<script>
  (function (window) {
    // Base URL to use for non-CNAME URLs.
    BB.baseUrl = 'https://bitbucket.org';

    BB.images = {
      invitation: 'https://d3oaxc4q5k2d6q.cloudfront.net/m/ab1188947552/img/icons/fugue/card_address.png',
      noAvatar: 'https://d3oaxc4q5k2d6q.cloudfront.net/m/ab1188947552/img/default_avatar/16/user_blue.png'
    };
    BB.user = {"username": "mxxie", "displayName": "Mengjun Xie", "firstName": "Mengjun", "avatarUrl": "https://secure.gravatar.com/avatar/fd28904c71ae2ce3d72a2839ee61fcdc?d=https%3A%2F%2Fd3oaxc4q5k2d6q.cloudfront.net%2Fm%2Fab1188947552%2Fimg%2Fdefault_avatar%2F32%2Fuser_blue.png\u0026s=32", "lastName": "Xie", "isTeam": false, "isSshEnabled": true, "isKbdShortcutsEnabled": true, "id": 281341, "isAuthenticated": true};
    BB.repo || (BB.repo = {});
    
      BB.repo.id = 2434744;
      BB.repo.scm = 'git';
      BB.repo.readonly = false;
      
      
        BB.repo.language = 'python';
        BB.repo.pygmentsLanguage = 'python';
      
      
        BB.repo.slug = 'ae\u002Dsna\u002Dclean';
      
      
        BB.repo.owner = {};
        BB.repo.owner.username = 'h0cked';
        BB.repo.owner.is_team = false;
      
      
        BB.repo.creator = {};
        BB.repo.creator.username = 'h0cked';
      
      // Coerce `BB.repo` to a string to get
      // "davidchambers/mango" or whatever.
      BB.repo.toString = function () {
        return BB.cname ? this.slug : '{owner.username}/{slug}'.format(this);
      }
      
        BB.changeset = '422b55ca2c2bfbca28d3b179514b1d271ce38b2c'
      
      
    
    window.setInterval(BB.localize, 60 * 1000);
    $(document).on('ready pjax:end', function () { BB.localize(); });
  })(window);
</script>


<script>
    // Bitbucket Google Analytics
    // NOTE: these will not fire in development. In debug mode it just logs them to console.
    (function (window) {
        // Track the main pageview to the Bitbucket GA account.
        BB.gaqPush(['_trackPageview']);
        // Track the main pageview to the Atlassian GA account.
        BB.gaqPush(['atl._trackPageview']);

        


        

        // Include GA commands from sub-templates
        

        (function () {
            var ga = document.createElement('script');
            ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
            ga.setAttribute('async', 'true');
            document.documentElement.firstChild.appendChild(ga);
        }());
    })(window);
</script>



</body>
</html>
