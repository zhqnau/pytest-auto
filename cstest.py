

def find_element(self,driver,locator,is_displayed=True,index=0,text=''):
    """
    Find element using the given condition..

    :param driver:
    :param para_list: [method, value] eg : ['id','add_btn']
    :param is_displayed: True : Only the element shown on the page will be returned.    False: Element will also be returned no matter is shown or hidden.
    :param index: If more than one element is found, driver will return the specified element by index.  e.g: element 0,1,2 is found and the index is set to by 2, the element 2 will be returned.
    :param text: Only the element contains the specified text will be returned.
    :return: Found element.
    """
    elements = self.find_elements(driver,locator,is_displayed=is_displayed,text=text)
    if len(elements)>0 and index < len(elements):
        return elements[index]
    else:
        return elements[0]



index = 1
eles = [10]
print(len(eles))
if len(eles) > 0 and index < len(eles):
    print(eles[index])
elif index > len(eles) :
    print("超出长度")
elif len(eles) == 0 :
    print("定位元素为空")
else:
    print(eles[0])
