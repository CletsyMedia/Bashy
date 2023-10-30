{"payload":{"allShortcutsEnabled":false,"fileTree":{"0x08-python-more_classes":{"items":[{"name":"__pycache__","path":"0x08-python-more_classes/__pycache__","contentType":"directory"},{"name":"0-rectangle.py","path":"0x08-python-more_classes/0-rectangle.py","contentType":"file"},{"name":"1-rectangle.py","path":"0x08-python-more_classes/1-rectangle.py","contentType":"file"},{"name":"101-nqueens.py","path":"0x08-python-more_classes/101-nqueens.py","contentType":"file"},{"name":"2-rectangle.py","path":"0x08-python-more_classes/2-rectangle.py","contentType":"file"},{"name":"3-rectangle.py","path":"0x08-python-more_classes/3-rectangle.py","contentType":"file"},{"name":"4-rectangle.py","path":"0x08-python-more_classes/4-rectangle.py","contentType":"file"},{"name":"5-rectangle.py","path":"0x08-python-more_classes/5-rectangle.py","contentType":"file"},{"name":"6-rectangle.py","path":"0x08-python-more_classes/6-rectangle.py","contentType":"file"},{"name":"7-rectangle.py","path":"0x08-python-more_classes/7-rectangle.py","contentType":"file"},{"name":"8-rectangle.py","path":"0x08-python-more_classes/8-rectangle.py","contentType":"file"},{"name":"9-rectangle.py","path":"0x08-python-more_classes/9-rectangle.py","contentType":"file"},{"name":"README.md","path":"0x08-python-more_classes/README.md","contentType":"file"}],"totalCount":13},"":{"items":[{"name":"0x00-python-hello_world","path":"0x00-python-hello_world","contentType":"directory"},{"name":"0x01-python-if_else_loops_functions","path":"0x01-python-if_else_loops_functions","contentType":"directory"},{"name":"0x02-python-import_modules","path":"0x02-python-import_modules","contentType":"directory"},{"name":"0x03-python-data_structures","path":"0x03-python-data_structures","contentType":"directory"},{"name":"0x04-python-more_data_structures","path":"0x04-python-more_data_structures","contentType":"directory"},{"name":"0x05-python-exceptions","path":"0x05-python-exceptions","contentType":"directory"},{"name":"0x06-python-classes","path":"0x06-python-classes","contentType":"directory"},{"name":"0x07-python-test_driven_development","path":"0x07-python-test_driven_development","contentType":"directory"},{"name":"0x08-python-more_classes","path":"0x08-python-more_classes","contentType":"directory"},{"name":"0x09-python-everything_is_object","path":"0x09-python-everything_is_object","contentType":"directory"},{"name":"0x0A-python-inheritance","path":"0x0A-python-inheritance","contentType":"directory"},{"name":"0x0B-python-input_output","path":"0x0B-python-input_output","contentType":"directory"},{"name":"0x0C-python-almost_a_circle","path":"0x0C-python-almost_a_circle","contentType":"directory"},{"name":"__pycache__","path":"__pycache__","contentType":"directory"},{"name":"README.md","path":"README.md","contentType":"file"}],"totalCount":15}},"fileTreeProcessingTime":6.419417999999999,"foldersToFetch":[],"reducedMotionEnabled":null,"repo":{"id":686988503,"defaultBranch":"main","name":"alx-higher_level_programming","ownerLogin":"Nkechi-Christabel","currentUserCanPush":false,"isFork":false,"isEmpty":false,"createdAt":"2023-09-04T11:24:41.000Z","ownerAvatar":"https://avatars.githubusercontent.com/u/49942946?v=4","public":true,"private":false,"isOrgOwned":false},"symbolsExpanded":false,"treeExpanded":true,"refInfo":{"name":"main","listCacheKey":"v0:1693827076.0","canEdit":false,"refType":"branch","currentOid":"3840c894544cc15e940404fadb661d463babc973"},"path":"0x08-python-more_classes/5-rectangle.py","currentUser":null,"blob":{"rawLines":["#!/usr/bin/python3","","\"\"\"","This module defines a class Rectangle.","","It is based on the 4-rectangle.py module.","\"\"\"","","","class Rectangle:","    \"\"\"A class that defines a rectangle.\"\"\"","","    def __init__(self, width=0, height=0):","        \"\"\"","        Initialize a new Rectangle instance.","","        Args:","            width (int, optional): The width of the rectangle (default is 0).","            height (int, optional): The height of the rectangle (default is 0).","        \"\"\"","        self.width = width","        self.height = height","","    @property","    def width(self):","        \"\"\"","        Get the width of the rectangle.","","        Returns:","            int: The width of the rectangle.","        \"\"\"","        return self.__width","","    @width.setter","    def width(self, value):","        \"\"\"","        Set the width of the rectangle.","","        Args:","            value (int): The new width value.","","        Raises:","            TypeError: If the width is not an integer.","            ValueError: If the width is less than 0.","        \"\"\"","        if not isinstance(value, int):","            raise TypeError(\"width must be an integer\")","        if value < 0:","            raise ValueError(\"width must be >= 0\")","        self.__width = value","","    @property","    def height(self):","        \"\"\"","        Get the height of the rectangle.","","        Returns:","            int: The height of the rectangle.","        \"\"\"","        return self.__height","","    @height.setter","    def height(self, value):","        \"\"\"","        Set the height of the rectangle.","","        Args:","            value (int): The new height value.","","        Raises:","            TypeError: If the height is not an integer.","            ValueError: If the height is less than 0.","        \"\"\"","        if not isinstance(value, int):","            raise TypeError(\"height must be an integer\")","        if value < 0:","            raise ValueError(\"height must be >= 0\")","        self.__height = value","","    def area(self):","        \"\"\"","        Calculate and return the area of the rectangle.","","        Returns:","            int: The area of the rectangle.","        \"\"\"","        return self.width * self.height","","    def perimeter(self):","        \"\"\"","        Calculate and return the perimeter of the rectangle.","","        Returns:","            int: The perimeter of the rectangle.","        \"\"\"","        if self.width == 0 or self.height == 0:","            return 0","        return 2 * (self.width + self.height)","","    def __str__(self):","        \"\"\"","        Return a string representation of the rectangle using '#' characters.","","        Returns:","            str: A string representation of the rectangle.","        \"\"\"","        if self.width == 0 or self.height == 0:","            return \"\"","","        return \"\\n\".join([\"#\" * self.width for _ in range(self.height)])","","    def __repr__(self):","        \"\"\"","        Return a string representation of the rectangle for eval().","","        Returns:","            str: A formal string representation of the rectangle.","        \"\"\"","        return f\"Rectangle({self.width}, {self.height})\"","","    def __del__(self):","        \"\"\"","        Print a message when an instance of Rectangle is deleted.","        \"\"\"","        print(\"Bye rectangle...\")"],"stylingDirectives":[[{"start":0,"end":18,"cssClass":"pl-c"}],[],[{"start":0,"end":3,"cssClass":"pl-s"}],[{"start":0,"end":38,"cssClass":"pl-s"}],[{"start":0,"end":0,"cssClass":"pl-s"}],[{"start":0,"end":41,"cssClass":"pl-s"}],[{"start":0,"end":3,"cssClass":"pl-s"}],[],[],[{"start":0,"end":5,"cssClass":"pl-k"},{"start":6,"end":15,"cssClass":"pl-v"}],[{"start":4,"end":43,"cssClass":"pl-s"}],[],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":16,"cssClass":"pl-en"},{"start":17,"end":21,"cssClass":"pl-s1"},{"start":23,"end":28,"cssClass":"pl-s1"},{"start":28,"end":29,"cssClass":"pl-c1"},{"start":29,"end":30,"cssClass":"pl-c1"},{"start":32,"end":38,"cssClass":"pl-s1"},{"start":38,"end":39,"cssClass":"pl-c1"},{"start":39,"end":40,"cssClass":"pl-c1"}],[{"start":8,"end":11,"cssClass":"pl-s"}],[{"start":0,"end":44,"cssClass":"pl-s"}],[{"start":0,"end":0,"cssClass":"pl-s"}],[{"start":0,"end":13,"cssClass":"pl-s"}],[{"start":0,"end":77,"cssClass":"pl-s"}],[{"start":0,"end":79,"cssClass":"pl-s"}],[{"start":0,"end":11,"cssClass":"pl-s"}],[{"start":8,"end":12,"cssClass":"pl-s1"},{"start":13,"end":18,"cssClass":"pl-s1"},{"start":19,"end":20,"cssClass":"pl-c1"},{"start":21,"end":26,"cssClass":"pl-s1"}],[{"start":8,"end":12,"cssClass":"pl-s1"},{"start":13,"end":19,"cssClass":"pl-s1"},{"start":20,"end":21,"cssClass":"pl-c1"},{"start":22,"end":28,"cssClass":"pl-s1"}],[],[{"start":4,"end":13,"cssClass":"pl-en"},{"start":5,"end":13,"cssClass":"pl-s1"}],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":13,"cssClass":"pl-en"},{"start":14,"end":18,"cssClass":"pl-s1"}],[{"start":8,"end":11,"cssClass":"pl-s"}],[{"start":0,"end":39,"cssClass":"pl-s"}],[{"start":0,"end":0,"cssClass":"pl-s"}],[{"start":0,"end":16,"cssClass":"pl-s"}],[{"start":0,"end":44,"cssClass":"pl-s"}],[{"start":0,"end":11,"cssClass":"pl-s"}],[{"start":8,"end":14,"cssClass":"pl-k"},{"start":15,"end":19,"cssClass":"pl-s1"},{"start":20,"end":27,"cssClass":"pl-s1"}],[],[{"start":4,"end":17,"cssClass":"pl-en"},{"start":5,"end":10,"cssClass":"pl-s1"},{"start":11,"end":17,"cssClass":"pl-s1"}],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":13,"cssClass":"pl-en"},{"start":14,"end":18,"cssClass":"pl-s1"},{"start":20,"end":25,"cssClass":"pl-s1"}],[{"start":8,"end":11,"cssClass":"pl-s"}],[{"start":0,"end":39,"cssClass":"pl-s"}],[{"start":0,"end":0,"cssClass":"pl-s"}],[{"start":0,"end":13,"cssClass":"pl-s"}],[{"start":0,"end":45,"cssClass":"pl-s"}],[{"start":0,"end":0,"cssClass":"pl-s"}],[{"start":0,"end":15,"cssClass":"pl-s"}],[{"start":0,"end":54,"cssClass":"pl-s"}],[{"start":0,"end":52,"cssClass":"pl-s"}],[{"start":0,"end":11,"cssClass":"pl-s"}],[{"start":8,"end":10,"cssClass":"pl-k"},{"start":11,"end":14,"cssClass":"pl-c1"},{"start":15,"end":25,"cssClass":"pl-en"},{"start":26,"end":31,"cssClass":"pl-s1"},{"start":33,"end":36,"cssClass":"pl-s1"}],[{"start":12,"end":17,"cssClass":"pl-k"},{"start":18,"end":27,"cssClass":"pl-v"},{"start":28,"end":54,"cssClass":"pl-s"}],[{"start":8,"end":10,"cssClass":"pl-k"},{"start":11,"end":16,"cssClass":"pl-s1"},{"start":17,"end":18,"cssClass":"pl-c1"},{"start":19,"end":20,"cssClass":"pl-c1"}],[{"start":12,"end":17,"cssClass":"pl-k"},{"start":18,"end":28,"cssClass":"pl-v"},{"start":29,"end":49,"cssClass":"pl-s"}],[{"start":8,"end":12,"cssClass":"pl-s1"},{"start":13,"end":20,"cssClass":"pl-s1"},{"start":21,"end":22,"cssClass":"pl-c1"},{"start":23,"end":28,"cssClass":"pl-s1"}],[],[{"start":4,"end":13,"cssClass":"pl-en"},{"start":5,"end":13,"cssClass":"pl-s1"}],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":14,"cssClass":"pl-en"},{"start":15,"end":19,"cssClass":"pl-s1"}],[{"start":8,"end":11,"cssClass":"pl-s"}],[{"start":0,"end":40,"cssClass":"pl-s"}],[{"start":0,"end":0,"cssClass":"pl-s"}],[{"start":0,"end":16,"cssClass":"pl-s"}],[{"start":0,"end":45,"cssClass":"pl-s"}],[{"start":0,"end":11,"cssClass":"pl-s"}],[{"start":8,"end":14,"cssClass":"pl-k"},{"start":15,"end":19,"cssClass":"pl-s1"},{"start":20,"end":28,"cssClass":"pl-s1"}],[],[{"start":4,"end":18,"cssClass":"pl-en"},{"start":5,"end":11,"cssClass":"pl-s1"},{"start":12,"end":18,"cssClass":"pl-s1"}],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":14,"cssClass":"pl-en"},{"start":15,"end":19,"cssClass":"pl-s1"},{"start":21,"end":26,"cssClass":"pl-s1"}],[{"start":8,"end":11,"cssClass":"pl-s"}],[{"start":0,"end":40,"cssClass":"pl-s"}],[{"start":0,"end":0,"cssClass":"pl-s"}],[{"start":0,"end":13,"cssClass":"pl-s"}],[{"start":0,"end":46,"cssClass":"pl-s"}],[{"start":0,"end":0,"cssClass":"pl-s"}],[{"start":0,"end":15,"cssClass":"pl-s"}],[{"start":0,"end":55,"cssClass":"pl-s"}],[{"start":0,"end":53,"cssClass":"pl-s"}],[{"start":0,"end":11,"cssClass":"pl-s"}],[{"start":8,"end":10,"cssClass":"pl-k"},{"start":11,"end":14,"cssClass":"pl-c1"},{"start":15,"end":25,"cssClass":"pl-en"},{"start":26,"end":31,"cssClass":"pl-s1"},{"start":33,"end":36,"cssClass":"pl-s1"}],[{"start":12,"end":17,"cssClass":"pl-k"},{"start":18,"end":27,"cssClass":"pl-v"},{"start":28,"end":55,"cssClass":"pl-s"}],[{"start":8,"end":10,"cssClass":"pl-k"},{"start":11,"end":16,"cssClass":"pl-s1"},{"start":17,"end":18,"cssClass":"pl-c1"},{"start":19,"end":20,"cssClass":"pl-c1"}],[{"start":12,"end":17,"cssClass":"pl-k"},{"start":18,"end":28,"cssClass":"pl-v"},{"start":29,"end":50,"cssClass":"pl-s"}],[{"start":8,"end":12,"cssClass":"pl-s1"},{"start":13,"end":21,"cssClass":"pl-s1"},{"start":22,"end":23,"cssClass":"pl-c1"},{"start":24,"end":29,"cssClass":"pl-s1"}],[],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":12,"cssClass":"pl-en"},{"start":13,"end":17,"cssClass":"pl-s1"}],[{"start":8,"end":11,"cssClass":"pl-s"}],[{"start":0,"end":55,"cssClass":"pl-s"}],[{"start":0,"end":0,"cssClass":"pl-s"}],[{"start":0,"end":16,"cssClass":"pl-s"}],[{"start":0,"end":43,"cssClass":"pl-s"}],[{"start":0,"end":11,"cssClass":"pl-s"}],[{"start":8,"end":14,"cssClass":"pl-k"},{"start":15,"end":19,"cssClass":"pl-s1"},{"start":20,"end":25,"cssClass":"pl-s1"},{"start":26,"end":27,"cssClass":"pl-c1"},{"start":28,"end":32,"cssClass":"pl-s1"},{"start":33,"end":39,"cssClass":"pl-s1"}],[],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":17,"cssClass":"pl-en"},{"start":18,"end":22,"cssClass":"pl-s1"}],[{"start":8,"end":11,"cssClass":"pl-s"}],[{"start":0,"end":60,"cssClass":"pl-s"}],[{"start":0,"end":0,"cssClass":"pl-s"}],[{"start":0,"end":16,"cssClass":"pl-s"}],[{"start":0,"end":48,"cssClass":"pl-s"}],[{"start":0,"end":11,"cssClass":"pl-s"}],[{"start":8,"end":10,"cssClass":"pl-k"},{"start":11,"end":15,"cssClass":"pl-s1"},{"start":16,"end":21,"cssClass":"pl-s1"},{"start":22,"end":24,"cssClass":"pl-c1"},{"start":25,"end":26,"cssClass":"pl-c1"},{"start":27,"end":29,"cssClass":"pl-c1"},{"start":30,"end":34,"cssClass":"pl-s1"},{"start":35,"end":41,"cssClass":"pl-s1"},{"start":42,"end":44,"cssClass":"pl-c1"},{"start":45,"end":46,"cssClass":"pl-c1"}],[{"start":12,"end":18,"cssClass":"pl-k"},{"start":19,"end":20,"cssClass":"pl-c1"}],[{"start":8,"end":14,"cssClass":"pl-k"},{"start":15,"end":16,"cssClass":"pl-c1"},{"start":17,"end":18,"cssClass":"pl-c1"},{"start":20,"end":24,"cssClass":"pl-s1"},{"start":25,"end":30,"cssClass":"pl-s1"},{"start":31,"end":32,"cssClass":"pl-c1"},{"start":33,"end":37,"cssClass":"pl-s1"},{"start":38,"end":44,"cssClass":"pl-s1"}],[],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":15,"cssClass":"pl-en"},{"start":16,"end":20,"cssClass":"pl-s1"}],[{"start":8,"end":11,"cssClass":"pl-s"}],[{"start":0,"end":77,"cssClass":"pl-s"}],[{"start":0,"end":0,"cssClass":"pl-s"}],[{"start":0,"end":16,"cssClass":"pl-s"}],[{"start":0,"end":58,"cssClass":"pl-s"}],[{"start":0,"end":11,"cssClass":"pl-s"}],[{"start":8,"end":10,"cssClass":"pl-k"},{"start":11,"end":15,"cssClass":"pl-s1"},{"start":16,"end":21,"cssClass":"pl-s1"},{"start":22,"end":24,"cssClass":"pl-c1"},{"start":25,"end":26,"cssClass":"pl-c1"},{"start":27,"end":29,"cssClass":"pl-c1"},{"start":30,"end":34,"cssClass":"pl-s1"},{"start":35,"end":41,"cssClass":"pl-s1"},{"start":42,"end":44,"cssClass":"pl-c1"},{"start":45,"end":46,"cssClass":"pl-c1"}],[{"start":12,"end":18,"cssClass":"pl-k"},{"start":19,"end":21,"cssClass":"pl-s"}],[],[{"start":8,"end":14,"cssClass":"pl-k"},{"start":15,"end":19,"cssClass":"pl-s"},{"start":16,"end":18,"cssClass":"pl-cce"},{"start":20,"end":24,"cssClass":"pl-en"},{"start":26,"end":29,"cssClass":"pl-s"},{"start":30,"end":31,"cssClass":"pl-c1"},{"start":32,"end":36,"cssClass":"pl-s1"},{"start":37,"end":42,"cssClass":"pl-s1"},{"start":43,"end":46,"cssClass":"pl-k"},{"start":47,"end":48,"cssClass":"pl-s1"},{"start":49,"end":51,"cssClass":"pl-c1"},{"start":52,"end":57,"cssClass":"pl-en"},{"start":58,"end":62,"cssClass":"pl-s1"},{"start":63,"end":69,"cssClass":"pl-s1"}],[],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":16,"cssClass":"pl-en"},{"start":17,"end":21,"cssClass":"pl-s1"}],[{"start":8,"end":11,"cssClass":"pl-s"}],[{"start":0,"end":67,"cssClass":"pl-s"}],[{"start":0,"end":0,"cssClass":"pl-s"}],[{"start":0,"end":16,"cssClass":"pl-s"}],[{"start":0,"end":65,"cssClass":"pl-s"}],[{"start":0,"end":11,"cssClass":"pl-s"}],[{"start":8,"end":14,"cssClass":"pl-k"},{"start":15,"end":56,"cssClass":"pl-s"},{"start":27,"end":39,"cssClass":"pl-s1"},{"start":27,"end":28,"cssClass":"pl-kos"},{"start":28,"end":32,"cssClass":"pl-s1"},{"start":33,"end":38,"cssClass":"pl-s1"},{"start":38,"end":39,"cssClass":"pl-kos"},{"start":41,"end":54,"cssClass":"pl-s1"},{"start":41,"end":42,"cssClass":"pl-kos"},{"start":42,"end":46,"cssClass":"pl-s1"},{"start":47,"end":53,"cssClass":"pl-s1"},{"start":53,"end":54,"cssClass":"pl-kos"}],[],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":15,"cssClass":"pl-en"},{"start":16,"end":20,"cssClass":"pl-s1"}],[{"start":8,"end":11,"cssClass":"pl-s"}],[{"start":0,"end":65,"cssClass":"pl-s"}],[{"start":0,"end":11,"cssClass":"pl-s"}],[{"start":8,"end":13,"cssClass":"pl-en"},{"start":14,"end":32,"cssClass":"pl-s"}]],"csv":null,"csvError":null,"dependabotInfo":{"showConfigurationBanner":false,"configFilePath":null,"networkDependabotPath":"/Nkechi-Christabel/alx-higher_level_programming/network/updates","dismissConfigurationNoticePath":"/settings/dismiss-notice/dependabot_configuration_notice","configurationNoticeDismissed":null,"repoAlertsPath":"/Nkechi-Christabel/alx-higher_level_programming/security/dependabot","repoSecurityAndAnalysisPath":"/Nkechi-Christabel/alx-higher_level_programming/settings/security_analysis","repoOwnerIsOrg":false,"currentUserCanAdminRepo":false},"displayName":"5-rectangle.py","displayUrl":"https://github.com/Nkechi-Christabel/alx-higher_level_programming/blob/main/0x08-python-more_classes/5-rectangle.py?raw=true","headerInfo":{"blobSize":"3.07 KB","deleteInfo":{"deleteTooltip":"You must be signed in to make or propose changes"},"editInfo":{"editTooltip":"You must be signed in to make or propose changes"},"ghDesktopPath":"https://desktop.github.com","gitLfsPath":null,"onBranch":true,"shortPath":"0525750","siteNavLoginPath":"/login?return_to=https%3A%2F%2Fgithub.com%2FNkechi-Christabel%2Falx-higher_level_programming%2Fblob%2Fmain%2F0x08-python-more_classes%2F5-rectangle.py","isCSV":false,"isRichtext":false,"toc":null,"lineInfo":{"truncatedLoc":"125","truncatedSloc":"99"},"mode":"file"},"image":false,"isCodeownersFile":null,"isPlain":false,"isValidLegacyIssueTemplate":false,"issueTemplateHelpUrl":"https://docs.github.com/articles/about-issue-and-pull-request-templates","issueTemplate":null,"discussionTemplate":null,"language":"Python","languageID":303,"large":false,"loggedIn":false,"newDiscussionPath":"/Nkechi-Christabel/alx-higher_level_programming/discussions/new","newIssuePath":"/Nkechi-Christabel/alx-higher_level_programming/issues/new","planSupportInfo":{"repoIsFork":null,"repoOwnedByCurrentUser":null,"requestFullPath":"/Nkechi-Christabel/alx-higher_level_programming/blob/main/0x08-python-more_classes/5-rectangle.py","showFreeOrgGatedFeatureMessage":null,"showPlanSupportBanner":null,"upgradeDataAttributes":null,"upgradePath":null},"publishBannersInfo":{"dismissActionNoticePath":"/settings/dismiss-notice/publish_action_from_dockerfile","dismissStackNoticePath":"/settings/dismiss-notice/publish_stack_from_file","releasePath":"/Nkechi-Christabel/alx-higher_level_programming/releases/new?marketplace=true","showPublishActionBanner":false,"showPublishStackBanner":false},"rawBlobUrl":"https://github.com/Nkechi-Christabel/alx-higher_level_programming/raw/main/0x08-python-more_classes/5-rectangle.py","renderImageOrRaw":false,"richText":null,"renderedFileInfo":null,"shortPath":null,"tabSize":8,"topBannersInfo":{"overridingGlobalFundingFile":false,"globalPreferredFundingPath":null,"repoOwner":"Nkechi-Christabel","repoName":"alx-higher_level_programming","showInvalidCitationWarning":false,"citationHelpUrl":"https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-on-github/about-citation-files","showDependabotConfigurationBanner":false,"actionsOnboardingTip":null},"truncated":false,"viewable":true,"workflowRedirectUrl":null,"symbols":{"timedOut":false,"notAnalyzed":false,"symbols":[{"name":"Rectangle","kind":"class","identStart":118,"identEnd":127,"extentStart":112,"extentEnd":3146,"fullyQualifiedName":"Rectangle","identUtf16":{"start":{"lineNumber":9,"utf16Col":6},"end":{"lineNumber":9,"utf16Col":15}},"extentUtf16":{"start":{"lineNumber":9,"utf16Col":0},"end":{"lineNumber":124,"utf16Col":33}}},{"name":"__init__","kind":"function","identStart":182,"identEnd":190,"extentStart":178,"extentEnd":514,"fullyQualifiedName":"Rectangle.__init__","identUtf16":{"start":{"lineNumber":12,"utf16Col":8},"end":{"lineNumber":12,"utf16Col":16}},"extentUtf16":{"start":{"lineNumber":12,"utf16Col":4},"end":{"lineNumber":21,"utf16Col":28}}},{"name":"width","kind":"function","identStart":538,"identEnd":543,"extentStart":534,"extentEnd":705,"fullyQualifiedName":"Rectangle.width","identUtf16":{"start":{"lineNumber":24,"utf16Col":8},"end":{"lineNumber":24,"utf16Col":13}},"extentUtf16":{"start":{"lineNumber":24,"utf16Col":4},"end":{"lineNumber":31,"utf16Col":27}}},{"name":"width","kind":"function","identStart":733,"identEnd":738,"extentStart":729,"extentEnd":1199,"fullyQualifiedName":"Rectangle.width","identUtf16":{"start":{"lineNumber":34,"utf16Col":8},"end":{"lineNumber":34,"utf16Col":13}},"extentUtf16":{"start":{"lineNumber":34,"utf16Col":4},"end":{"lineNumber":49,"utf16Col":28}}},{"name":"height","kind":"function","identStart":1223,"identEnd":1229,"extentStart":1219,"extentEnd":1394,"fullyQualifiedName":"Rectangle.height","identUtf16":{"start":{"lineNumber":52,"utf16Col":8},"end":{"lineNumber":52,"utf16Col":14}},"extentUtf16":{"start":{"lineNumber":52,"utf16Col":4},"end":{"lineNumber":59,"utf16Col":28}}},{"name":"height","kind":"function","identStart":1423,"identEnd":1429,"extentStart":1419,"extentEnd":1897,"fullyQualifiedName":"Rectangle.height","identUtf16":{"start":{"lineNumber":62,"utf16Col":8},"end":{"lineNumber":62,"utf16Col":14}},"extentUtf16":{"start":{"lineNumber":62,"utf16Col":4},"end":{"lineNumber":77,"utf16Col":29}}},{"name":"area","kind":"function","identStart":1907,"identEnd":1911,"extentStart":1903,"extentEnd":2100,"fullyQualifiedName":"Rectangle.area","identUtf16":{"start":{"lineNumber":79,"utf16Col":8},"end":{"lineNumber":79,"utf16Col":12}},"extentUtf16":{"start":{"lineNumber":79,"utf16Col":4},"end":{"lineNumber":86,"utf16Col":39}}},{"name":"perimeter","kind":"function","identStart":2110,"identEnd":2119,"extentStart":2106,"extentEnd":2393,"fullyQualifiedName":"Rectangle.perimeter","identUtf16":{"start":{"lineNumber":88,"utf16Col":8},"end":{"lineNumber":88,"utf16Col":17}},"extentUtf16":{"start":{"lineNumber":88,"utf16Col":4},"end":{"lineNumber":97,"utf16Col":45}}},{"name":"__str__","kind":"function","identStart":2403,"identEnd":2410,"extentStart":2399,"extentEnd":2740,"fullyQualifiedName":"Rectangle.__str__","identUtf16":{"start":{"lineNumber":99,"utf16Col":8},"end":{"lineNumber":99,"utf16Col":15}},"extentUtf16":{"start":{"lineNumber":99,"utf16Col":4},"end":{"lineNumber":109,"utf16Col":72}}},{"name":"__repr__","kind":"function","identStart":2750,"identEnd":2758,"extentStart":2746,"extentEnd":2998,"fullyQualifiedName":"Rectangle.__repr__","identUtf16":{"start":{"lineNumber":111,"utf16Col":8},"end":{"lineNumber":111,"utf16Col":16}},"extentUtf16":{"start":{"lineNumber":111,"utf16Col":4},"end":{"lineNumber":118,"utf16Col":56}}},{"name":"__del__","kind":"function","identStart":3008,"identEnd":3015,"extentStart":3004,"extentEnd":3146,"fullyQualifiedName":"Rectangle.__del__","identUtf16":{"start":{"lineNumber":120,"utf16Col":8},"end":{"lineNumber":120,"utf16Col":15}},"extentUtf16":{"start":{"lineNumber":120,"utf16Col":4},"end":{"lineNumber":124,"utf16Col":33}}}]}},"copilotInfo":null,"copilotAccessAllowed":false,"csrf_tokens":{"/Nkechi-Christabel/alx-higher_level_programming/branches":{"post":"_ukCwVACdJt6CB5HdHHGgDL0GRKodBKIzRsRd1lC04aVbU2iMMnk-REAjOHalSKKB7Z9e7zro1fypC9KOEdw9g"},"/repos/preferences":{"post":"waXGNiLIfLApYWU9OadA8Wx1b15B-LpUPiMnPkZ5mwy4P3lBc3oJfzsuQKi3CV1a_2vV-k8GII9xTRsyVZA2tg"}}},"title":"alx-higher_level_programming/0x08-python-more_classes/5-rectangle.py at main · Nkechi-Christabel/alx-higher_level_programming"}