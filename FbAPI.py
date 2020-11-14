# EAAFHxuBHYiUBAHDEK4r1VyzUnd81UfuY8U17ddGADRsodhEJIrwNpiwUb1oX7nelzLD7vgZC7UeqPcxN0PQH6vs27TZA9DWPZANiC3ZBUsraOKCEKZCfUOwuzKG2z9YG6fnakne3mRdLUlTAa9PHVuyznqZApXZBUX1kXuSxbPmMAZDZD


# curl -X POST -H "Content-Type: application/json" -d '{
#   "messaging_type": "<MESSAGING_TYPE>",
#   "recipient": {
#     "id": "<PSID>"
#   },
#   "message": {
#     "text": "hello, world!"
#   }
# }' "https://graph.facebook.com/v9.0/me/messages?access_token=<PAGE_ACCESS_TOKEN>"
#
# client: mercury
# action_type: ma-type:user-generated-message
# body: tetewtew
# ephemeral_ttl_mode: 0
# has_attachment: false
# message_id: 6733071050665075659
# offline_threading_id: 6733071050665075659
# other_user_fbid: 114824030434924
# source: source:titan:web
# specific_to_list[0]: fbid:114824030434924
# specific_to_list[1]: fbid:1044299211
# tags[0]:
# timestamp: 1605289232889
# to_list_md5: 5c27f2541bfe81495b826298ffb5af7f
# __user: 1044299211
# __a: 1
# __dyn: 7AgNeQ4qmfxd2u6Xolg9odoKEaQjFwgoqzob4q2i5U4e2C3Cm7V8C3q2OUuKewXyE4mdwJKdx3wnoOEiwvUe8hxG18wzwxgeGwbqq0KbG7ooxu15wm8aU2WxOfwDwrE88hwKx-8wgolzUO9w4XwyDKi8wGwFyE6K2C8xK1nwBgK7qxS18wc61uG3G1lwGwHzUuw8y4Ueo2swkEbElxm0zEnwhE2LyE4a
# __csr:
# __req: 1i
# __beoa: 0
# __pc: PHASED:DEFAULT
# dpr: 2
# __ccg: EXCELLENT
# __rev: 1002975274
# __s: dqdurz:ubim0b:fwqxpv
# __hsi: 6894664658741140200-0
# __comet_req: 0
# cquick: jsc_c_lw
# cquick_token: AQ7C10-8hvaaja4eEN4
# ctarget: https%253A%252F%252Fwww.facebook.com
# fb_dtsg: AQF4YnEdimIb:AQG-frOMwfKR
# jazoest: 22091
# __spin_r: 1002975274
# __spin_b: trunk
# __spin_t: 1605285306


# Send message
    # check for complete laod
    # wait = WebDriverWait(driver, 10)
    # element = wait.until(EC.element_to_be_clickable((By.ID, "js_10")))

    # element = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='New message']")))
    # element = driver.find_element_by_id("js_10")

    # content = driver.find_element_by_xpath("//div[@aria-label='New message']")

    # if element is None:
    #     print("sdada")
    # else:
    #     print(element)

    # elem = driver.find_element_by_name("q")
    # elem.clear()
    # elem.send_keys("pycon")
    # elem.send_keys(Keys.RETURN)