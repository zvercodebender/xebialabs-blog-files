<#assign hostForUrl=container.host.address?string>
<#if container.hostname?has_content>
	<#assign hostForUrl=container.hostname>
</#if>
<#assign adminUrl = container.protocol + "://" + hostForUrl + ":" + container.port>

<#list container.wlstProperties as prop>
    key=$(echo ${prop} | cut -f1 -d=)
    val=$(echo ${prop} | cut -f2 -d=)
    echo "${r"${key}"} = ${r"${val}"}" 
    echo "${r"${key}"}=${r"${val}"}" >> /tmp/wlst.properties
</#list>
echo "======================================="

export DEPLOYIT_WLST_PASSWORD=${container.password}
${container.getWlstPath()} -i ${script} ${container.username} ${adminUrl}
res=$?
if [ $res != 0 ] ; then
	exit $res
fi
rm /tmp/wlst.properties
