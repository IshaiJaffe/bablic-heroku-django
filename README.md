[Bablic](http://addons.heroku.com/bablic) is an [add-on](http://addons.heroku.com) for easy website localization.

Adding Bablic to a web application gives you the abillity to control your site localization from the cloud.
No i18n infrastructure needed! It doesn't matter in which language your site is written and you don't need to use any guidelines to start the integration.
The installation takes a minute for any site.
We provude you a translation memory system on our dashboard, or simply on top of your site.
Bablic also offers:
- Automatic integration to human translation services.
- Machine translation.
- CSS modifications support.
- Bi-directional support.
- Language navigation widget.
- Image replacement.


## Provisioning the add-on

Bablic can be attached to a Heroku application via the  CLI:

<div class="callout" markdown="1">
A list of all plans available can be found [here](http://addons.heroku.com/bablic).
</div>

    :::term
    $ heroku addons:add bablic
    -----> Adding bablic to sharp-mountain-4005... done, v18 (free)
    -----> Localization is set from "en" to "es"

 You'll notice the message saying you're site localization is set from english to spanish, those are the defaults locale codes.
 To define your site locale codes on provision:

    $ heroku addons:add bablic --original=<ORIGINAL_LOCALE_CODE> --target=<TARGET_LOCALE_CODES>

 For example:

    $ heroku addons:add bablic --original=fr --target="de,hi"
    -----> Adding bablic to sharp-mountain-4005... done, v18 (free)
    -----> Localization is set from "fr" to "de,hi"


 Once Bablic has been added, a `BABLIC_ID` and a `BABLIC_SNIPPET` setting will be available in the app configuration. The `BABLIC_SNIPPET` is the client-side code that will be added to your HTML layout files. to integrate your web pages. This can be confirmed using the `heroku config:get` command.

    :::term
    $ heroku config:get BABLIC_ID
    50101180ea87740200000137

After installing Bablic the application should be configured to fully integrate with the add-on.

## Using with Django


### Installation

Create a context processor that will add the snippet to every template context:


	from django.conf import settings # import the settings file

	import os
	BABLIC_SNIPPET = os.environ.get('BABLIC_SNIPPET','')
	
	def bablic(request):
		return {'BABLIC_SNIPPET': BABLIC_SNIPPET, 'locale': BABLIC_SNIPPET and request.session and request.session.get('locale')}
 
Add the context processor in your settings.py

	TEMPLATE_CONTEXT_PROCESSORS = (
		"django.contrib.auth.context_processors.auth",
		"django.core.context_processors.debug",
		"django.core.context_processors.i18n",
		"django.core.context_processors.media",
		"django.core.context_processors.static",
		"django.contrib.messages.context_processors.messages",
		"app_name.context_processors.bablic")

Add the snippet injection in you layout html file
	<html>
		<head>
		...
		</head>
	<body>
		{{ BABLIC_SNIPPET|safe }}
	

If you want to define the selected locale from the backend set the `bablic.locale` after the snippet

	<html>
		<head>
		...
		</head>
	<body>
		{{ BABLIC_SNIPPET|safe }}
		{% if locale %}
		<script>
			bablic.locale = "{{ locale }}";
		</script>
		{% endif %}


### Configuration

Exclude specific elements:

    <div data-bablic-exclude>
	    Text not for translation
    </div>


Include specific elements, even if their parents are excluded:

    <div data-bablic-exclude>
	Text not for translation
        <span data-bablic-include>
	     Text for translation
        </span>
    </div>

## Using with NodeJS

in your layout.ejs file

    <html>
    ....
        <body>
            <%= process.env.BABLIC_SNIPPET || '' %>
    ....

## Using with Rails 3.x

in your layout.erb file ( or any other html template file you're using )

    <html>
     ....
        <body>
            <%= ENV('BABLIC_SNIPPET') %>
    .....

## Dashboard

<div class="callout" markdown="1">
For more information on the features available within the Bablic dashboard please see the docs at [www.bablic.com/docs](www.bablic.com/docs).
</div>

The Bablic dashboard allows you to: add or remove languages, translate content, revise bad translations, change locale detection & adjust language navigiation widget.

![Bablic Dashboard](http://i.imgur.com/FkuUw.png "Bablic Dashboard")

The dashboard can be accessed via the CLI:

    :::term
    $ heroku addons:open bablic
    Opening bablic for sharp-mountain-4005…

or by visiting the [Heroku apps web interface](http://heroku.com/myapps) and selecting the application in question. Select Bablic from the Add-ons menu.

![Bablic Add-ons Dropdown](http://f.cl.ly/items/1B090n1P0d3W0I0R172r/addons.png "Bablic Add-ons Dropdown")

## Migrating between plans

<div class="note" markdown="1">Application owners should carefully manage the migration timing to ensure proper application function during the migration process.</div>

Use the `heroku addons:upgrade` command to migrate to a new plan.

    :::term
    $ heroku addons:upgrade bablic:newplan
    -----> Upgrading bablic:newplan to sharp-mountain-4005... done, v18 ($49/mo)
           Your plan has been updated to: bablic:newplan

## Removing the add-on

Bablic can be removed via the  CLI.

<div class="warning" markdown="1">This will destroy all associated data and cannot be undone!</div>

    :::term
    $ heroku addons:remove bablic
    -----> Removing bablic from sharp-mountain-4005... done, v20 (free)

Before removing Bablic a data export can be performed from Bablic Dashboard.

## Support

All Bablic support and runtime issues should be submitted via on of the [Heroku Support channels](support-channels). Any non-support related issues or product feedback is welcome at [support@bablic.com](support@bablic.com).

## Additional resources

Additional resources are available at:

* [Bablic Site](http://www.bablic.com)
