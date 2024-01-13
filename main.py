import flet as ft
import dictionary
import joblib

data=[]
CGPA=[]
#font size
sz=16
winwidth=900
winheight=780
title="GPA Predictor"
def page1(page: ft.Page):
    page.theme_mode=ft.ThemeMode.LIGHT
    page.title = title
    page.window_width = winwidth
    page.window_height = winheight
    page.window_resizable=False

    # pw = ft.Text(bottom=50, right=50)
    # page.overlay.append(pw)

    def page1data(e):
        data.append(BS4.value)
        data.append(preferential_treatment.value)
        data.append(transport_timings_wastage.value)
        data.append(teachers_kindness_female_students.value)
        data.append(cheating_online_exams_impact.value)
        data.append(guidance.value)
        data.append(hostelite_guidance.value)
        data.append(tvf_preparation.value)
        CGPA.append(BS4.value)
        page.update()
        page.clean()
        page2(page)

    b = ft.ElevatedButton("Next", on_click=page1data,width=150,height=60)
    # Drop down menus
    preferential_treatment=ft.Dropdown(
        width=40,
        options=[
            ft.dropdown.Option(value, key) for key, value in dictionary.preferential_treatment_impact_environment_encoding.items()
            ],
        value=2)

    transport_timings_wastage = ft.Dropdown(
        width=40,
        options=[
            ft.dropdown.Option(value, key) for key, value in
            dictionary.transport_timings_wastage_encoding.items()
        ],
        value=2)

    teachers_kindness_female_students = ft.Dropdown(
        width=40,
        options=[
            ft.dropdown.Option(value, key) for key, value in
            dictionary.teachers_kindness_female_students_encoding.items()
        ],
        value=2)

    cheating_online_exams_impact = ft.Dropdown(
        width=40,
        options=[
            ft.dropdown.Option(value, key) for key, value in
            dictionary.cheating_online_exams_impact_encoding.items()
        ],
        value=2)

    guidance = ft.Dropdown(
        width=40,
        options=[
            ft.dropdown.Option(value, key) for key, value in
            dictionary.guidance_encoding.items()
        ],
        value=1)

    hostelite_guidance = ft.Dropdown(
        width=40,
        options=[
            ft.dropdown.Option(value, key) for key, value in
            dictionary.hostelite_guidance_encoding.items()
        ],
        value=2)

    tvf_preparation = ft.Dropdown(
        width=40,
        options=[
            ft.dropdown.Option(value, key) for key, value in
            dictionary.tvf_preparation_encoding.items()
        ],
        value=2)





    # Text field
    BS4=ft.TextField(hint_text="X.XX", autofocus=False, content_padding=ft.padding.only(left=10),
                    width=60, text_size=12,
                    border_color=ft.colors.BLACK26, focused_border_color=ft.colors.BLUE_ACCENT)


    # adding to page
    page.add(
        ft.ResponsiveRow(
            [
                ft.Container(
                    ft.Text(value="Result Prediction", color=ft.colors.BLACK, text_align=ft.TextAlign.CENTER,size=20),
                    padding=10,
                    col={"sm": 4, "md": 13, "xl": 10}
                ),
            ]
        ),

        ft.ResponsiveRow(
            [
                ft.Container(
                    ft.Text(value="SGPA in BS fourth semester", color=ft.colors.BLACK,size=sz,
                            text_align=ft.TextAlign.LEFT),
                    padding=10,
                    height=50,
                    alignment=ft.alignment.bottom_left,
                    col={"sm": 4, "md": 8, "xl": 10}
                ),
                ft.Container(
                    BS4,
                    col={"sm": 4, "md": 4, "xl": 10}
                )
            ]
        ),

        ft.ResponsiveRow(
            [
                ft.Container(
                    ft.Text(value="Preferential treatment impact on classroom environment",size=sz,
                            color=ft.colors.BLACK,text_align=ft.TextAlign.LEFT),
                    padding=10,
                    height=50,
                    alignment=ft.alignment.bottom_left,
                    col={"sm": 4, "md": 8, "xl": 10}
                ),
                ft.Container(
                    preferential_treatment,
                    width=10,
                    col={"sm": 6, "md": 4, "xl": 2}
                ),
            ],
        ),

        ft.ResponsiveRow(
            [
                ft.Container(
                    ft.Text(value="Time wastage due to official transport timings can impact grades",size=sz,
                            color=ft.colors.BLACK,
                            text_align=ft.TextAlign.LEFT),
                    padding=10,
                    height=50,
                    alignment=ft.alignment.bottom_left,
                    col={"sm": 4, "md": 8, "xl": 10}
                ),
                ft.Container(
                    transport_timings_wastage,
                    width=10,
                    col={"sm": 6, "md": 4, "xl": 2}
                ),
            ],
        ),
        #D
        ft.ResponsiveRow(
            [
                ft.Container(
                    ft.Text(value="Teachers showing kindness towards female students can impact grades",size=sz,
                            color=ft.colors.BLACK,
                            text_align=ft.TextAlign.LEFT),
                    padding=10,
                    height=70,
                    alignment=ft.alignment.bottom_left,
                    col={"sm": 4, "md": 8, "xl": 10}
                ),
                ft.Container(
                    teachers_kindness_female_students,
                    width=10,
                    col={"sm": 6, "md": 4, "xl": 2}
                ),
            ],
        ),

        # E
        ft.ResponsiveRow(
            [
                ft.Container(
                    ft.Text(value="Ease of cheating in online exams impact on motivation",size=sz,
                            color=ft.colors.BLACK,
                            text_align=ft.TextAlign.LEFT),
                    padding=10,
                    height=50,
                    alignment=ft.alignment.bottom_left,
                    col={"sm": 4, "md": 8, "xl": 10}
                ),
                ft.Container(
                    cheating_online_exams_impact,
                    width=10,
                    col={"sm": 6, "md": 4, "xl": 2}
                ),
            ],
        ),
        # F
        ft.ResponsiveRow(
            [
                ft.Container(
                    ft.Text(value="Guidance can impact grades",size=sz,
                            color=ft.colors.BLACK,
                            text_align=ft.TextAlign.LEFT),
                    padding=10,
                    height=50,
                    alignment=ft.alignment.bottom_left,
                    col={"sm": 4, "md": 8, "xl": 10}
                ),
                ft.Container(
                    guidance,
                    width=10,
                    col={"sm": 6, "md": 4, "xl": 2}
                ),
            ],
        ),
        # G
        ft.ResponsiveRow(
            [
                ft.Container(
                    ft.Text(value="Hostilities connections and guidance with seniors can impact grades",size=sz,
                            color=ft.colors.BLACK,
                            text_align=ft.TextAlign.LEFT),
                    padding=10,
                    height=50,
                    alignment=ft.alignment.bottom_left,
                    col={"sm": 4, "md": 8, "xl": 10}
                ),
                ft.Container(
                    hostelite_guidance,
                    width=10,
                    col={"sm": 6, "md": 4, "xl": 2}
                ),
            ],
        ),
        # H
        ft.ResponsiveRow(
            [
                ft.Container(
                    ft.Text(value="TVFs are not very well prepared for lectures which impact grades",size=sz,
                            color=ft.colors.BLACK,
                            text_align=ft.TextAlign.LEFT),
                    padding=10,
                    height=50,
                    alignment=ft.alignment.bottom_left,
                    col={"sm": 4, "md": 8, "xl": 10}
                ),
                ft.Container(
                    tvf_preparation,
                    width=10,
                    col={"sm": 6, "md": 4, "xl": 2}
                ),
            ],
        ),
        b
    )


def page2(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.title = title
    page.window_width = winwidth
    page.window_height = winheight
    page.window_resizable = False

    def page2data(e):
        data.append(Gender.value)
        data.append(discrimination_impact.value)
        data.append(tvf_grading.value)
        data.append(BS1.value)
        data.append(senior_instructors_technical.value)
        data.append(BS3.value)
        data.append(lecture_mode.value)
        data.append(classes_unannounced.value)
        data.append(tvf_rescheduling.value)
        CGPA.append(BS1.value)
        CGPA.append(BS3.value)
        page.update()
        page.clean()
        page3(page)

    b = ft.ElevatedButton("Next", on_click=page2data, width=150, height=60)
    # drop down
    Gender = ft.Dropdown(
        width=40,
        options=[
            ft.dropdown.Option(value, key) for key, value in
            dictionary.gender_encoding.items()
        ],
        value=1)

    discrimination_impact = ft.Dropdown(
        width=40,
        options=[
            ft.dropdown.Option(value, key) for key, value in
            dictionary.discrimination_impact_focus_interest_encoding.items()
        ],
        value=1)

    tvf_grading = ft.Dropdown(
        width=40,
        options=[
            ft.dropdown.Option(value, key) for key, value in
            dictionary.tvf_grading_beliefs_encoding.items()
        ],
        value=1)

    senior_instructors_technical = ft.Dropdown(
        width=40,
        options=[
            ft.dropdown.Option(value, key) for key, value in
            dictionary.senior_instructors_technical_expertise_encoding.items()
        ],
        value=1)

    lecture_mode = ft.Dropdown(
        width=40,
        options=[
            ft.dropdown.Option(value, key) for key, value in
            dictionary.lecture_mode_encoding.items()
        ],
        value=1)
    classes_unannounced = ft.Dropdown(
        width=40,
        options=[
            ft.dropdown.Option(value, key) for key, value in
            dictionary.impact_missing_classes_unannounced_quizzes_encoding.items()
        ],
        value=1)
    tvf_rescheduling = ft.Dropdown(
        width=40,
        options=[
            ft.dropdown.Option(value, key) for key, value in
            dictionary.tvf_rescheduling_encoding.items()
        ],
        value=1)

    # text field
    BS1 = ft.TextField(hint_text="X.XX", autofocus=False, content_padding=ft.padding.only(left=10),
                       width=60, text_size=12,
                       border_color=ft.colors.BLACK26, focused_border_color=ft.colors.BLUE_ACCENT)
    BS3 = ft.TextField(hint_text="X.XX", autofocus=False, content_padding=ft.padding.only(left=10),
                       width=60, text_size=12,
                       border_color=ft.colors.BLACK26, focused_border_color=ft.colors.BLUE_ACCENT)

    page.add(
        # L
        ft.ResponsiveRow(
            [
                ft.Container(
                    ft.Text(value="SGPA in BS first semester",size=sz,
                            color=ft.colors.BLACK,
                            text_align=ft.TextAlign.LEFT),
                    padding=10,
                    height=50,
                    alignment=ft.alignment.bottom_left,
                    col={"sm": 4, "md": 8, "xl": 10}
                ),
                ft.Container(
                    BS1,
                    width=10,
                    col={"sm": 6, "md": 4, "xl": 2}
                ),
            ],
        ),
        # N
        ft.ResponsiveRow(
            [
                ft.Container(
                    ft.Text(value="SGPA in BS third semester",size=sz,
                            color=ft.colors.BLACK,
                            text_align=ft.TextAlign.LEFT),
                    padding=10,
                    height=50,
                    alignment=ft.alignment.bottom_left,
                    col={"sm": 4, "md": 8, "xl": 10}
                ),
                ft.Container(
                    BS3,
                    width=10,
                    col={"sm": 6, "md": 4, "xl": 2}
                ),
            ],
        ),
        # I
        ft.ResponsiveRow(
            [
                ft.Container(
                    ft.Text(value="Gender",size=sz,
                            color=ft.colors.BLACK,
                            text_align=ft.TextAlign.LEFT),
                    padding=10,
                    height=50,
                    alignment=ft.alignment.bottom_left,
                    col={"sm": 4, "md": 8, "xl": 10}
                ),
                ft.Container(
                    Gender,
                    width=10,
                    col={"sm": 6, "md": 4, "xl": 2}
                ),
            ],
        ),
        # J
        ft.ResponsiveRow(
            [
                ft.Container(
                    ft.Text(value="Discrimination impact on focus and interest in classes which can impact grades",
                            size=sz,
                            color=ft.colors.BLACK,
                            text_align=ft.TextAlign.LEFT),
                    padding=10,
                    height=70,
                    alignment=ft.alignment.bottom_left,
                    col={"sm": 4, "md": 8, "xl": 10}
                ),
                ft.Container(
                    discrimination_impact,
                    width=10,
                    col={"sm": 6, "md": 4, "xl": 2}
                ),
            ],
        ),
        # K
        ft.ResponsiveRow(
            [
                ft.Container(
                    ft.Text(value="TVFs grading based on their beliefs can impact grade",size=sz,
                            color=ft.colors.BLACK,
                            text_align=ft.TextAlign.LEFT),
                    padding=10,
                    height=50,
                    alignment=ft.alignment.bottom_left,
                    col={"sm": 4, "md": 8, "xl": 10}
                ),
                ft.Container(
                    tvf_grading,
                    width=10,
                    col={"sm": 6, "md": 4, "xl": 2}
                ),
            ],
        ),

        # M
        ft.ResponsiveRow(
            [
                ft.Container(
                    ft.Text(value="Senior instructors lack of technical expertise in online class impact grade",size=sz,
                            color=ft.colors.BLACK,
                            text_align=ft.TextAlign.LEFT),
                    padding=10,
                    height=70,
                    alignment=ft.alignment.bottom_left,
                    col={"sm": 4, "md": 8, "xl": 10}
                ),
                ft.Container(
                    senior_instructors_technical,
                    width=10,
                    col={"sm": 6, "md": 4, "xl": 2}
                ),
            ],
        ),

        # 0
        ft.ResponsiveRow(
            [
                ft.Container(
                    ft.Text(value="Which lecture mode help understand better",size=sz,
                            color=ft.colors.BLACK,
                            text_align=ft.TextAlign.LEFT),
                    padding=10,
                    height=50,
                    alignment=ft.alignment.bottom_left,
                    col={"sm": 4, "md": 8, "xl": 10}
                ),
                ft.Container(
                    lecture_mode,
                    width=10,
                    col={"sm": 6, "md": 4, "xl": 2}
                ),
            ],
        ),

        # P
        ft.ResponsiveRow(
            [
                ft.Container(
                    ft.Text(value="Cannot miss classes due to un-announced quizzes which impacts grades", size=sz,
                            color=ft.colors.BLACK,
                            text_align=ft.TextAlign.LEFT),
                    padding=10,
                    height=70,
                    alignment=ft.alignment.bottom_left,
                    col={"sm": 4, "md": 8, "xl": 10}
                ),
                ft.Container(
                    classes_unannounced,
                    width=10,
                    col={"sm": 6, "md": 4, "xl": 2}
                ),
            ],
        ),
        # q
        ft.ResponsiveRow(
            [
                ft.Container(
                    ft.Text(value="TVFs reschedule classes that negatively impacts my performance", size=sz,
                            color=ft.colors.BLACK,
                            text_align=ft.TextAlign.LEFT),
                    padding=10,
                    height=50,
                    alignment=ft.alignment.bottom_left,
                    col={"sm": 4, "md": 8, "xl": 10}
                ),
                ft.Container(
                    tvf_rescheduling,
                    width=10,
                    col={"sm": 6, "md": 4, "xl": 2}
                ),
            ],
        ),

        b
    )


def page3(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.title = title
    page.window_width = winwidth
    page.window_height = winheight
    page.window_resizable = False

    def page3data(e):
        data.append(tvf_curriculum_awareness.value)
        data.append(youtube_chatGPT.value)
        data.append(mobile_usage.value)
        data.append(surprise_quizzes.value)
        data.append(study_mode.value)
        data.append(basic_education.value)
        data.append(campus_resources.value)
        data.append(maximum_mobile_usage.value)
        data.append(quizzes_stressfulness.value)
        page.update()
        page.clean()
        page4(page)



    b = ft.ElevatedButton("Next", on_click=page3data, width=150, height=60)
    # drop down
    tvf_curriculum_awareness = ft.Dropdown(
        width=40,
        options=[
            ft.dropdown.Option(value, key) for key, value in
            dictionary.tvf_curriculum_awareness_encoding.items()
        ],
        value=1)

    youtube_chatGPT =  ft.Dropdown(
        width=40,
        options=[
            ft.dropdown.Option(value, key) for key, value in
            dictionary.youtube_chatGPT_usage_encoding.items()
        ],
        value=1)

    mobile_usage = ft.Dropdown(
        width=40,
        options=[
            ft.dropdown.Option(value, key) for key, value in
            dictionary.lowest_mobile_usage_encoding.items()
        ],
        value=1)
    surprise_quizzes = ft.Dropdown(
        width=40,
        options=[
            ft.dropdown.Option(value, key) for key, value in
            dictionary.lack_of_preparation_surprise_quizzes_encoding.items()
        ],
        value=1)

    study_mode = ft.Dropdown(
        width=40,
        options=[
            ft.dropdown.Option(value, key) for key, value in
            dictionary.preferred_study_mode_encoding.items()
        ],
        value=1)

    basic_education = ft.Dropdown(
        width=40,
        options=[
            ft.dropdown.Option(value, key) for key, value in
            dictionary.basic_education_encoding.items()
        ],
        value=1)

    campus_resources= ft.Dropdown(
        width=40,
        options=[
            ft.dropdown.Option(value, key) for key, value in
            dictionary.hostelite_campus_resources_encoding.items()
        ],
        value=1)

    maximum_mobile_usage = ft.Dropdown(
        width=40,
        options=[
            ft.dropdown.Option(value, key) for key, value in
            dictionary.maximum_mobile_usage_encoding.items()
        ],
        value=1)

    quizzes_stressfulness = ft.Dropdown(
        width=40,
        options=[
            ft.dropdown.Option(value, key) for key, value in
            dictionary.unannounced_quizzes_stressfulness_encoding.items()
        ],
        value=1)


    page.add(
        # R
        ft.ResponsiveRow(
            [
                ft.Container(
                    ft.Text(value="TVFs are not aware of the university's curriculum which can impact grades", size=sz,
                            color=ft.colors.BLACK,
                            text_align=ft.TextAlign.LEFT),
                    padding=10,
                    height=70,
                    alignment=ft.alignment.bottom_left,
                    col={"sm": 4, "md": 8, "xl": 10}
                ),
                ft.Container(
                    tvf_curriculum_awareness,
                    width=10,
                    col={"sm": 6, "md": 4, "xl": 2}
                ),
            ],
        ),

        # S
        ft.ResponsiveRow(
            [
                ft.Container(
                    ft.Text(value="I frequently usage of YouTube or Chat GPT for understanding concepts", size=sz,
                            color=ft.colors.BLACK,
                            text_align=ft.TextAlign.LEFT),
                    padding=10,
                    height=70,
                    alignment=ft.alignment.bottom_left,
                    col={"sm": 4, "md": 8, "xl": 10}
                ),
                ft.Container(
                    youtube_chatGPT,
                    width=10,
                    col={"sm": 6, "md": 4, "xl": 2}
                ),
            ],
        ),
        # T
        ft.ResponsiveRow(
            [
                ft.Container(
                    ft.Text(value="My lowest mobile usage is", size=sz,
                            color=ft.colors.BLACK,
                            text_align=ft.TextAlign.LEFT),
                    padding=10,
                    height=50,
                    alignment=ft.alignment.bottom_left,
                    col={"sm": 4, "md": 8, "xl": 10}
                ),
                ft.Container(
                    mobile_usage,
                    width=10,
                    col={"sm": 6, "md": 4, "xl": 2}
                ),
            ],
        ),

        # u
        ft.ResponsiveRow(
            [
                ft.Container(
                    ft.Text(value="Lack of preparation for surprise quizzes which impact my interest in subject", size=sz,
                            color=ft.colors.BLACK,
                            text_align=ft.TextAlign.LEFT),
                    padding=10,
                    height=70,
                    alignment=ft.alignment.bottom_left,
                    col={"sm": 4, "md": 8, "xl": 10}
                ),
                ft.Container(
                    surprise_quizzes,
                    width=10,
                    col={"sm": 6, "md": 4, "xl": 2}
                ),
            ],
        ),
        # v
        ft.ResponsiveRow(
            [
                ft.Container(
                    ft.Text(value="My preferable mode of study is", size=sz,
                            color=ft.colors.BLACK,
                            text_align=ft.TextAlign.LEFT),
                    padding=10,
                    height=50,
                    alignment=ft.alignment.bottom_left,
                    col={"sm": 4, "md": 8, "xl": 10}
                ),
                ft.Container(
                    study_mode,
                    width=10,
                    col={"sm": 6, "md": 4, "xl": 2}
                ),
            ],
        ),
        # w
        ft.ResponsiveRow(
            [
                ft.Container(
                    ft.Text(value="My basic education is", size=sz,
                            color=ft.colors.BLACK,
                            text_align=ft.TextAlign.LEFT),
                    padding=10,
                    height=50,
                    alignment=ft.alignment.bottom_left,
                    col={"sm": 4, "md": 8, "xl": 10}
                ),
                ft.Container(
                    basic_education,
                    width=10,
                    col={"sm": 6, "md": 4, "xl": 2}
                ),
            ],
        ),

        # x
        ft.ResponsiveRow(
            [
                ft.Container(
                    ft.Text(value="Hostelites have better access to campus resources and benefit of group study", size=sz,
                            color=ft.colors.BLACK,
                            text_align=ft.TextAlign.LEFT),
                    padding=10,
                    height=70,
                    alignment=ft.alignment.bottom_left,
                    col={"sm": 4, "md": 8, "xl": 10}
                ),
                ft.Container(
                    campus_resources,
                    width=10,
                    col={"sm": 6, "md": 4, "xl": 2}
                ),
            ],
        ),
        # y
        ft.ResponsiveRow(
            [
                ft.Container(
                    ft.Text(value="My maximum mobile usage",
                            size=sz,
                            color=ft.colors.BLACK,
                            text_align=ft.TextAlign.LEFT),
                    padding=10,
                    height=50,
                    alignment=ft.alignment.bottom_left,
                    col={"sm": 4, "md": 8, "xl": 10}
                ),
                ft.Container(
                    maximum_mobile_usage,
                    width=10,
                    col={"sm": 6, "md": 4, "xl": 2}
                ),
            ],
        ),
        # z
        ft.ResponsiveRow(
            [
                ft.Container(
                    ft.Text(value="Un-announced quizzes are stressful, cause anxiety and pressure on students",
                            size=sz,
                            color=ft.colors.BLACK,
                            text_align=ft.TextAlign.LEFT),
                    padding=10,
                    height=70,
                    alignment=ft.alignment.bottom_left,
                    col={"sm": 4, "md": 8, "xl": 10}
                ),
                ft.Container(
                    quizzes_stressfulness,
                    width=10,
                    col={"sm": 6, "md": 4, "xl": 2}
                ),
            ],
        ),

        b
    )
    page.update()


def page4(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.title = title
    page.window_width = winwidth
    page.window_height = winheight
    page.window_resizable = False

    def page4data(e):
        data.append(interest_encoding.value)
        data.append(number_of_students.value)
        data.append(daily_subject.value)
        data.append(non_technical.value)
        data.append(health_issues.value)
        data.append(lecture_duration.value)
        data.append(scholarship.value)
        data.append(negative_impact.value)
        data.append(classroom_environment.value)
        page.update()
        page.clean()
        page5(page)

    b = ft.ElevatedButton("Next", on_click=page4data, width=150, height=60)

    # drop down
    interest_encoding = ft.Dropdown(
        width=40,
        options=[
            ft.dropdown.Option(value, key) for key, value in
            dictionary.program_interest_encoding.items()
        ],
        value=1)

    number_of_students = ft.Dropdown(
        width=40,
        options=[
            ft.dropdown.Option(value, key) for key, value in
            dictionary.number_of_students_encoding.items()
        ],
        value=1)

    daily_subject = ft.Dropdown(
        width=40,
        options=[
            ft.dropdown.Option(value, key) for key, value in
            dictionary.daily_subject_practice_encoding.items()
        ],
        value=1)

    non_technical = ft.Dropdown(
        width=40,
        options=[
            ft.dropdown.Option(value, key) for key, value in
            dictionary.daily_subject_practice_encoding.items()
        ],
        value=1)
    health_issues = ft.Dropdown(
        width=40,
        options=[
            ft.dropdown.Option(value, key) for key, value in
            dictionary.health_issues_performance_encoding.items()
        ],
        value=1)

    lecture_duration = ft.Dropdown(
        width=40,
        options=[
            ft.dropdown.Option(value, key) for key, value in
            dictionary.lecture_duration_encoding.items()
        ],
        value=1)

    scholarship = ft.Dropdown(
        width=40,
        options=[
            ft.dropdown.Option(value, key) for key, value in
            dictionary.scholarship_encoding.items()
        ],
        value=1)
    negative_impact = ft.Dropdown(
        width=40,
        options=[
            ft.dropdown.Option(value, key) for key, value in
            dictionary.negative_impact_unannounced_quizzes_encoding.items()
        ],
        value=1)
    classroom_environment = ft.Dropdown(
        width=40,
        options=[
            ft.dropdown.Option(value, key) for key, value in
            dictionary.classroom_environment_online_encoding.items()
        ],
        value=1)


    page.add(

        # AA
        ft.ResponsiveRow(
            [
                ft.Container(
                    ft.Text(value="I opted for this program of study because of my own interest",
                            size=sz,
                            color=ft.colors.BLACK,
                            text_align=ft.TextAlign.LEFT),
                    padding=10,
                    height=50,
                    alignment=ft.alignment.bottom_left,
                    col={"sm": 4, "md": 8, "xl": 10}
                ),
                ft.Container(
                    interest_encoding,
                    width=10,
                    col={"sm": 6, "md": 4, "xl": 2}
                ),
            ],
        ),
        # AB
        ft.ResponsiveRow(
            [
                ft.Container(
                    ft.Text(value="Number of students in class",
                            size=sz,
                            color=ft.colors.BLACK,
                            text_align=ft.TextAlign.LEFT),
                    padding=10,
                    height=50,
                    alignment=ft.alignment.bottom_left,
                    col={"sm": 4, "md": 8, "xl": 10}
                ),
                ft.Container(
                    number_of_students,
                    width=10,
                    col={"sm": 6, "md": 4, "xl": 2}
                ),
            ],
        ),
        # AC
        ft.ResponsiveRow(
            [
                ft.Container(
                    ft.Text(value="I prefer to revise the lectures daily or before the next class of the same subject",
                            size=sz,
                            color=ft.colors.BLACK,
                            text_align=ft.TextAlign.LEFT),
                    padding=10,
                    height=70,
                    alignment=ft.alignment.bottom_left,
                    col={"sm": 4, "md": 8, "xl": 10}
                ),
                ft.Container(
                    daily_subject,
                    width=10,
                    col={"sm": 6, "md": 4, "xl": 2}
                ),
            ],
        ),
        # AD
        ft.ResponsiveRow(
            [
                ft.Container(
                    ft.Text(value="I enjoy and perform well in non-technical courses",
                            size=sz,
                            color=ft.colors.BLACK,
                            text_align=ft.TextAlign.LEFT),
                    padding=10,
                    height=50,
                    alignment=ft.alignment.bottom_left,
                    col={"sm": 4, "md": 8, "xl": 10}
                ),
                ft.Container(
                    non_technical,
                    width=10,
                    col={"sm": 6, "md": 4, "xl": 2}
                ),
            ],
        ),
        # AE
        ft.ResponsiveRow(
            [
                ft.Container(
                    ft.Text(value="I often come across health issues that effect my academic performance",
                            size=sz,
                            color=ft.colors.BLACK,
                            text_align=ft.TextAlign.LEFT),
                    padding=10,
                    height=70,
                    alignment=ft.alignment.bottom_left,
                    col={"sm": 4, "md": 8, "xl": 10}
                ),
                ft.Container(
                    health_issues,
                    width=10,
                    col={"sm": 6, "md": 4, "xl": 2}
                ),
            ],
        ),
        # AF
        ft.ResponsiveRow(
            [
                ft.Container(
                    ft.Text(value="Does lecture duration effect grades ",
                            size=sz,
                            color=ft.colors.BLACK,
                            text_align=ft.TextAlign.LEFT),
                    padding=10,
                    height=50,
                    alignment=ft.alignment.bottom_left,
                    col={"sm": 4, "md": 8, "xl": 10}
                ),
                ft.Container(
                    lecture_duration,
                    width=10,
                    col={"sm": 6, "md": 4, "xl": 2}
                ),
            ],
        ),
        # AG
        ft.ResponsiveRow(
            [
                ft.Container(
                    ft.Text(value="Scholarship",
                            size=sz,
                            color=ft.colors.BLACK,
                            text_align=ft.TextAlign.LEFT),
                    padding=10,
                    height=50,
                    alignment=ft.alignment.bottom_left,
                    col={"sm": 4, "md": 8, "xl": 10}
                ),
                ft.Container(
                    scholarship,
                    width=10,
                    col={"sm": 6, "md": 4, "xl": 2}
                ),
            ],
        ),
        # AH
        ft.ResponsiveRow(
            [
                ft.Container(
                    ft.Text(value="Un-announced quizzes are waste of time, energy and are not effective",
                            size=sz,
                            color=ft.colors.BLACK,
                            text_align=ft.TextAlign.LEFT),
                    padding=10,
                    height=70,
                    alignment=ft.alignment.bottom_left,
                    col={"sm": 4, "md": 8, "xl": 10}
                ),
                ft.Container(
                    negative_impact,
                    width=10,
                    col={"sm": 6, "md": 4, "xl": 2}
                ),
            ],
        ),
        # AI
        ft.ResponsiveRow(
            [
                ft.Container(
                    ft.Text(value="A proper classroom environment is not possible to maintained in online environment",
                            size=sz,
                            color=ft.colors.BLACK,
                            text_align=ft.TextAlign.LEFT),
                    padding=10,
                    height=70,
                    alignment=ft.alignment.bottom_left,
                    col={"sm": 4, "md": 8, "xl": 10}
                ),
                ft.Container(
                    classroom_environment,
                    width=10,
                    col={"sm": 6, "md": 4, "xl": 2}
                ),
            ],
        ),

        b
    )

def page5(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.title = title
    page.window_width = winwidth
    page.window_height = winheight
    page.window_resizable = False

    def page4data(e):
        data.append(fathers_education.value)
        data.append(leniency_activeness.value)
        data.append(FM.value)
        data.append(intermediate_education.value)
        data.append(discrimination.value)
        data.append(instructor.value)
        data.append(tight_class.value)
        data.append(sitting_place.value)
        data.append(tvf_relationship.value)
        page.update()
        page.clean()
        page6(page)

    b = ft.ElevatedButton("Next", on_click=page4data, width=150, height=60)
    # drop down

    # drop down
    fathers_education = ft.Dropdown(
        width=40,
        options=[
            ft.dropdown.Option(value, key) for key, value in
            dictionary.fathers_education_encoding.items()
        ],
        value=1)
    leniency_activeness = ft.Dropdown(
        width=40,
        options=[
            ft.dropdown.Option(value, key) for key, value in
            dictionary.likelihood_leniency_activeness_encoding.items()
        ],
        value=1)

    intermediate_education = ft.Dropdown(
        width=40,
        options=[
            ft.dropdown.Option(value, key) for key, value in
            dictionary.intermediate_education_encoding.items()
        ],
        value=1)

    discrimination = ft.Dropdown(
        width=40,
        options=[
            ft.dropdown.Option(value, key) for key, value in
            dictionary.discrimination_impact_focus_interest_encoding.items()
        ],
        value=1)

    instructor = ft.Dropdown(
        width=40,
        options=[
            ft.dropdown.Option(value, key) for key, value in
            dictionary.instructor_missed_classes_encoding.items()
        ],
        value=1)

    tight_class = ft.Dropdown(
        width=40,
        options=[
            ft.dropdown.Option(value, key) for key, value in
            dictionary.tight_class_schedule_encoding.items()
        ],
        value=1)

    sitting_place= ft.Dropdown(
        width=40,
        options=[
            ft.dropdown.Option(value, key) for key, value in
            dictionary.sitting_place_encoding.items()
        ],
        value=1)
    tvf_relationship = ft.Dropdown(
        width=40,
        options=[
            ft.dropdown.Option(value, key) for key, value in
            dictionary.tvf_relationship_duration_encoding.items()
        ],
        value=1)
    # text field
    FM = ft.TextField(hint_text="X.XX", autofocus=False, content_padding=ft.padding.only(left=10),
                      width=60, text_size=12,
                      border_color=ft.colors.BLACK26, focused_border_color=ft.colors.BLUE_ACCENT)


    page.add(
        # Al
        ft.ResponsiveRow(
            [
                ft.Container(
                    ft.Text(value="Family members",
                            size=sz,
                            color=ft.colors.BLACK,
                            text_align=ft.TextAlign.LEFT),
                    padding=10,
                    height=50,
                    alignment=ft.alignment.bottom_left,
                    col={"sm": 4, "md": 8, "xl": 10}
                ),
                ft.Container(
                    FM,
                    width=10,
                    col={"sm": 6, "md": 4, "xl": 2}
                ),
            ],
        ),

        # AJ
        ft.ResponsiveRow(
            [
                ft.Container(
                    ft.Text(value="Father's education",
                            size=sz,
                            color=ft.colors.BLACK,
                            text_align=ft.TextAlign.LEFT),
                    padding=10,
                    height=50,
                    alignment=ft.alignment.bottom_left,
                    col={"sm": 4, "md": 8, "xl": 10}
                ),
                ft.Container(
                    fathers_education,
                    width=10,
                    col={"sm": 6, "md": 4, "xl": 2}
                ),
            ],
        ),
        # AK
        ft.ResponsiveRow(
            [
                ft.Container(
                    ft.Text(value="Likelihood of leniency based on student's activeness in class",
                            size=sz,
                            color=ft.colors.BLACK,
                            text_align=ft.TextAlign.LEFT),
                    padding=10,
                    height=50,
                    alignment=ft.alignment.bottom_left,
                    col={"sm": 4, "md": 8, "xl": 10}
                ),
                ft.Container(
                    leniency_activeness,
                    width=10,
                    col={"sm": 6, "md": 4, "xl": 2}
                ),
            ],
        ),

        # AM
        ft.ResponsiveRow(
            [
                ft.Container(
                    ft.Text(value="Intermediate education",
                            size=sz,
                            color=ft.colors.BLACK,
                            text_align=ft.TextAlign.LEFT),
                    padding=10,
                    height=50,
                    alignment=ft.alignment.bottom_left,
                    col={"sm": 4, "md": 8, "xl": 10}
                ),
                ft.Container(
                    intermediate_education,
                    width=10,
                    col={"sm": 6, "md": 4, "xl": 2}
                ),
            ],
        ),

        # AN
        ft.ResponsiveRow(
            [
                ft.Container(
                    ft.Text(value="Discrimination negatively effects my mental health and engagement in the class",
                            size=sz,
                            color=ft.colors.BLACK,
                            text_align=ft.TextAlign.LEFT),
                    padding=10,
                    height=70,
                    alignment=ft.alignment.bottom_left,
                    col={"sm": 4, "md": 8, "xl": 10}
                ),
                ft.Container(
                    discrimination,
                    width=10,
                    col={"sm": 6, "md": 4, "xl": 2}
                ),
            ],
        ),
        # AO
        ft.ResponsiveRow(
            [
                ft.Container(
                    ft.Text(value="Instructors miss lectures and arrange makeup classes that increases my burden",
                            size=sz,
                            color=ft.colors.BLACK,
                            text_align=ft.TextAlign.LEFT),
                    padding=10,
                    height=70,
                    alignment=ft.alignment.bottom_left,
                    col={"sm": 4, "md": 8, "xl": 10}
                ),
                ft.Container(
                    instructor,
                    width=10,
                    col={"sm": 6, "md": 4, "xl": 2}
                ),
            ],
        ),
        # Ap
        ft.ResponsiveRow(
            [
                ft.Container(
                    ft.Text(value="My classes schedule is usually very tight that hinders the process of learning",
                            size=sz,
                            color=ft.colors.BLACK,
                            text_align=ft.TextAlign.LEFT),
                    padding=10,
                    height=70,
                    alignment=ft.alignment.bottom_left,
                    col={"sm": 4, "md": 8, "xl": 10}
                ),
                ft.Container(
                    tight_class,
                    width=10,
                    col={"sm": 6, "md": 4, "xl": 2}
                ),
            ],
        ),
        # Aq
        ft.ResponsiveRow(
            [
                ft.Container(
                    ft.Text(value="Sitting place",
                            size=sz,
                            color=ft.colors.BLACK,
                            text_align=ft.TextAlign.LEFT),
                    padding=10,
                    height=50,
                    alignment=ft.alignment.bottom_left,
                    col={"sm": 4, "md": 8, "xl": 10}
                ),
                ft.Container(
                    sitting_place,
                    width=10,
                    col={"sm": 6, "md": 4, "xl": 2}
                ),
            ],
        ),
        # Ar
        ft.ResponsiveRow(
            [
                ft.Container(
                    ft.Text(value="TVFs relations with students is short so they are not sincere",
                            size=sz,
                            color=ft.colors.BLACK,
                            text_align=ft.TextAlign.LEFT),
                    padding=10,
                    height=50,
                    alignment=ft.alignment.bottom_left,
                    col={"sm": 4, "md": 8, "xl": 10}
                ),
                ft.Container(
                    tvf_relationship,
                    width=10,
                    col={"sm": 6, "md": 4, "xl": 2}
                ),
            ],
        ),

        b
    )

def page6(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.title = title
    page.window_width = winwidth
    page.window_height = winheight
    page.window_resizable = False

    def page4data(e):
        data.append(residence_place.value)
        data.append(technical_resources.value)
        data.append(exam_preparedness.value)
        data.append(hostelite_focus.value)
        data.append(recorded_lectures.value)
        data.append(lecture_language.value)
        data.append(tvf_assessment_results.value)
        data.append(social_media.value)
        data.append(study_time.value)
        page.update()
        page.clean()
        page7(page)

    b = ft.ElevatedButton("Next", on_click=page4data, width=150, height=60)
    # drop down

    # drop down
    residence_place = ft.Dropdown(
        width=40,
        options=[
            ft.dropdown.Option(value, key) for key, value in
            dictionary.residence_place_encoding.items()
        ],
        value=1)

    technical_resources = ft.Dropdown(
        width=40,
        options=[
            ft.dropdown.Option(value, key) for key, value in
            dictionary.technical_resources_disruption_encoding.items()
        ],
        value=1)

    exam_preparedness = ft.Dropdown(
        width=40,
        options=[
            ft.dropdown.Option(value, key) for key, value in
            dictionary.exam_preparedness_vs_stress_encoding.items()
        ],
        value=1)
    hostelite_focus = ft.Dropdown(
        width=40,
        options=[
            ft.dropdown.Option(value, key) for key, value in
            dictionary.hostelite_focus_encoding.items()
        ],
        value=1)

    recorded_lectures = ft.Dropdown(
        width=40,
        options=[
            ft.dropdown.Option(value, key) for key, value in
            dictionary.recorded_lectures_hobby_encoding.items()
        ],
        value=1)

    lecture_language = ft.Dropdown(
        width=40,
        options=[
            ft.dropdown.Option(value, key) for key, value in
            dictionary.lecture_language_encoding.items()
        ],
        value=1)

    tvf_assessment_results = ft.Dropdown(
        width=40,
        options=[
            ft.dropdown.Option(value, key) for key, value in
            dictionary.tvf_assessment_results_encoding.items()
        ],
        value=1)
    social_media = ft.Dropdown(
        width=40,
        options=[
            ft.dropdown.Option(value, key) for key, value in
            dictionary.social_media_distraction_encoding.items()
        ],
        value=1)

    study_time= ft.Dropdown(
        width=40,
        options=[
            ft.dropdown.Option(value, key) for key, value in
            dictionary.preferred_study_time_encoding.items()
        ],
        value=1)

    # Text field
    FM = ft.TextField(hint_text="X.XX", autofocus=False, content_padding=ft.padding.only(left=10),
                      width=60, text_size=12,
                      border_color=ft.colors.BLACK26, focused_border_color=ft.colors.BLUE_ACCENT)

    page.add(
        # AS
        ft.ResponsiveRow(
            [
                ft.Container(
                    ft.Text(value="Residence place",
                            size=sz,
                            color=ft.colors.BLACK,
                            text_align=ft.TextAlign.LEFT),
                    padding=10,
                    height=50,
                    alignment=ft.alignment.bottom_left,
                    col={"sm": 4, "md": 8, "xl": 10}
                ),
                ft.Container(
                    residence_place,
                    width=10,
                    col={"sm": 6, "md": 4, "xl": 2}
                ),
            ],
        ),
        # AT
        ft.ResponsiveRow(
            [
                ft.Container(
                    ft.Text(value="Lack of technical resources make it difficult to understand",
                            size=sz,
                            color=ft.colors.BLACK,
                            text_align=ft.TextAlign.LEFT),
                    padding=10,
                    height=50,
                    alignment=ft.alignment.bottom_left,
                    col={"sm": 4, "md": 8, "xl": 10}
                ),
                ft.Container(
                    technical_resources,
                    width=10,
                    col={"sm": 6, "md": 4, "xl": 2}
                ),
            ],
        ),
        # AU
        ft.ResponsiveRow(
            [
                ft.Container(
                    ft.Text(value="I am unable to attempt exam properly due to exam stress",
                            size=sz,
                            color=ft.colors.BLACK,
                            text_align=ft.TextAlign.LEFT),
                    padding=10,
                    height=50,
                    alignment=ft.alignment.bottom_left,
                    col={"sm": 4, "md": 8, "xl": 10}
                ),
                ft.Container(
                    exam_preparedness,
                    width=10,
                    col={"sm": 6, "md": 4, "xl": 2}
                ),
            ],
        ),
        # AV
        ft.ResponsiveRow(
            [
                ft.Container(
                    ft.Text(value="Hostilities can be more focused towards their studies"
                                  "whereas a day scholar may have a lot of distractions due to family issues.",
                            size=sz,
                            color=ft.colors.BLACK,
                            text_align=ft.TextAlign.LEFT),
                    padding=10,
                    height=70,
                    alignment=ft.alignment.bottom_left,
                    col={"sm": 4, "md": 8, "xl": 10}
                ),
                ft.Container(
                    hostelite_focus,
                    width=10,
                    col={"sm": 6, "md": 4, "xl": 2}
                ),
            ],
        ),
        # Aw
        ft.ResponsiveRow(
            [
                ft.Container(
                    ft.Text(value="It becomes a hobby to watch recorded lectures later on, so I try "
                                  "to cover a lot of content in a short time that becomes difficult to absorb.",
                            size=sz,
                            color=ft.colors.BLACK,
                            text_align=ft.TextAlign.LEFT),
                    padding=10,
                    height=70,
                    alignment=ft.alignment.bottom_left,
                    col={"sm": 4, "md": 8, "xl": 10}
                ),
                ft.Container(
                    recorded_lectures,
                    width=10,
                    col={"sm": 6, "md": 4, "xl": 2}
                ),
            ],
        ),
        # AX
        ft.ResponsiveRow(
            [
                ft.Container(
                    ft.Text(value="Lecture language",
                            size=sz,
                            color=ft.colors.BLACK,
                            text_align=ft.TextAlign.LEFT),
                    padding=10,
                    height=70,
                    alignment=ft.alignment.bottom_left,
                    col={"sm": 4, "md": 8, "xl": 10}
                ),
                ft.Container(
                    lecture_language,
                    width=10,
                    col={"sm": 6, "md": 4, "xl": 2}
                ),
            ],
        ),

        # AY
        ft.ResponsiveRow(
            [
                ft.Container(
                    ft.Text(value="TVFs do not provide assessment results timely",
                            size=sz,
                            color=ft.colors.BLACK,
                            text_align=ft.TextAlign.LEFT),
                    padding=10,
                    height=50,
                    alignment=ft.alignment.bottom_left,
                    col={"sm": 4, "md": 8, "xl": 10}
                ),
                ft.Container(
                    tvf_assessment_results,
                    width=10,
                    col={"sm": 6, "md": 4, "xl": 2}
                ),
            ],
        ),
        # AZ
        ft.ResponsiveRow(
            [
                ft.Container(
                    ft.Text(value="I am easily distracted by social media during online lectures",
                            size=sz,
                            color=ft.colors.BLACK,
                            text_align=ft.TextAlign.LEFT),
                    padding=10,
                    height=50,
                    alignment=ft.alignment.bottom_left,
                    col={"sm": 4, "md": 8, "xl": 10}
                ),
                ft.Container(
                    social_media,
                    width=10,
                    col={"sm": 6, "md": 4, "xl": 2}
                ),
            ],
        ),

        # BA
        ft.ResponsiveRow(
            [
                ft.Container(
                    ft.Text(value="My preferable time of study is",
                            size=sz,
                            color=ft.colors.BLACK,
                            text_align=ft.TextAlign.LEFT),
                    padding=10,
                    height=50,
                    alignment=ft.alignment.bottom_left,
                    col={"sm": 4, "md": 8, "xl": 10}
                ),
                ft.Container(
                    study_time,
                    width=10,
                    col={"sm": 6, "md": 4, "xl": 2}
                ),
            ],
        ),

        b
    )


def page7(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.title = title
    page.window_width = winwidth
    page.window_height = winheight
    page.window_resizable = False

    def page4data(e):
        data.append(interper.value)
        data.append(CR.value)
        data.append(BS2.value)
        data.append(Attendance.value)
        data.append(time_consumption.value)
        data.append(tvf_accessibility.value)
        data.append(lecture_material.value)
        data.append(conveying_concepts.value)
        data.append(MP.value)
        data.append(mothers_education.value)
        page.update()
        page.clean()
        CGPA.append(BS2.value)
        page8(page)

    b = ft.ElevatedButton("Next", on_click=page4data, width=150, height=60)
    # drop down

    # drop down
    CR = ft.Dropdown(
        width=40,
        options=[
            ft.dropdown.Option(value, key) for key, value in
            dictionary.preference_for_class_representative_encoding.items()
        ],
        value=1)

    Attendance = ft.Dropdown(
        width=40,
        options=[
            ft.dropdown.Option(value, key) for key, value in
            dictionary.attendance_encoding.items()
        ],
        value=1)

    time_consumption = ft.Dropdown(
        width=40,
        options=[
            ft.dropdown.Option(value, key) for key, value in
            dictionary.commuting_time_consumption_encoding.items()
        ],
        value=1)

    tvf_accessibility = ft.Dropdown(
        width=40,
        options=[
            ft.dropdown.Option(value, key) for key, value in
            dictionary.tvf_accessibility_encoding.items()
        ],
        value=1)

    lecture_material = ft.Dropdown(
        width=40,
        options=[
            ft.dropdown.Option(value, key) for key, value in
            dictionary.lecture_material_encoding.items()
        ],
        value=1)

    conveying_concepts = ft.Dropdown(
        width=40,
        options=[
            ft.dropdown.Option(value, key) for key, value in
            dictionary.difficulty_conveying_concepts_online_encoding.items()
        ],
        value=1)

    mothers_education= ft.Dropdown(
        width=40,
        options=[
            ft.dropdown.Option(value, key) for key, value in
            dictionary.mothers_education_encoding.items()
        ],
        value=1)

    # Text field
    interper = ft.TextField(hint_text="X.XX", autofocus=False, content_padding=ft.padding.only(left=10),
                      width=60, text_size=12,
                      border_color=ft.colors.BLACK26, focused_border_color=ft.colors.BLUE_ACCENT)

    BS2 = ft.TextField(hint_text="X.XX", autofocus=False, content_padding=ft.padding.only(left=10),
                      width=60, text_size=12,
                      border_color=ft.colors.BLACK26, focused_border_color=ft.colors.BLUE_ACCENT)
    MP = ft.TextField(hint_text="X.XX", autofocus=False, content_padding=ft.padding.only(left=10),
                       width=60, text_size=12,
                       border_color=ft.colors.BLACK26, focused_border_color=ft.colors.BLUE_ACCENT)
    page.add(
        # BB
        ft.ResponsiveRow(
            [
                ft.Container(
                    ft.Text(value="Intermediate percentage",
                            size=sz,
                            color=ft.colors.BLACK,
                            text_align=ft.TextAlign.LEFT),
                    padding=10,
                    height=50,
                    alignment=ft.alignment.bottom_left,
                    col={"sm": 4, "md": 8, "xl": 10}
                ),
                ft.Container(
                    interper,
                    width=10,
                    col={"sm": 6, "md": 4, "xl": 2}
                ),
            ],
        ),

        # BJ
        ft.ResponsiveRow(
            [
                ft.Container(
                    ft.Text(value="Matric percentage",
                            size=sz,
                            color=ft.colors.BLACK,
                            text_align=ft.TextAlign.LEFT),
                    padding=10,
                    height=50,
                    alignment=ft.alignment.bottom_left,
                    col={"sm": 4, "md": 8, "xl": 10}
                ),
                ft.Container(
                    MP,
                    width=10,
                    col={"sm": 6, "md": 4, "xl": 2}
                ),
            ],
        ),
        # BD
        ft.ResponsiveRow(
            [
                ft.Container(
                    ft.Text(value="SGPA in BS Second semester",
                            size=sz,
                            color=ft.colors.BLACK,
                            text_align=ft.TextAlign.LEFT),
                    padding=10,
                    height=50,
                    alignment=ft.alignment.bottom_left,
                    col={"sm": 4, "md": 8, "xl": 10}
                ),
                ft.Container(
                    BS2,
                    width=10,
                    col={"sm": 6, "md": 4, "xl": 2}
                ),
            ],
        ),
        # BC
        ft.ResponsiveRow(
            [
                ft.Container(
                    ft.Text(value="Class Representative is favored more than any ordinary student",
                            size=sz,
                            color=ft.colors.BLACK,
                            text_align=ft.TextAlign.LEFT),
                    padding=10,
                    height=50,
                    alignment=ft.alignment.bottom_left,
                    col={"sm": 4, "md": 8, "xl": 10}
                ),
                ft.Container(
                    CR,
                    width=10,
                    col={"sm": 6, "md": 4, "xl": 2}
                ),
            ],
        ),
        # BE
        ft.ResponsiveRow(
            [
                ft.Container(
                    ft.Text(value="Does attendance effect your grade",
                            size=sz,
                            color=ft.colors.BLACK,
                            text_align=ft.TextAlign.LEFT),
                    padding=10,
                    height=50,
                    alignment=ft.alignment.bottom_left,
                    col={"sm": 4, "md": 8, "xl": 10}
                ),
                ft.Container(
                    Attendance,
                    width=10,
                    col={"sm": 6, "md": 4, "xl": 2}
                ),
            ],
        ),
        # BF
        ft.ResponsiveRow(
            [
                ft.Container(
                    ft.Text(value="An ample amount of time is consumed on daily commuting "
                                  "and all energy is drained during travelling.",
                            size=sz,
                            color=ft.colors.BLACK,
                            text_align=ft.TextAlign.LEFT),
                    padding=10,
                    height=70,
                    alignment=ft.alignment.bottom_left,
                    col={"sm": 4, "md": 8, "xl": 10}
                ),
                ft.Container(
                    time_consumption,
                    width=10,
                    col={"sm": 6, "md": 4, "xl": 2}
                ),
            ],
        ),
        # BG
        ft.ResponsiveRow(
            [
                ft.Container(
                    ft.Text(value="TVFs are very difficult to access after class timings",
                            size=sz,
                            color=ft.colors.BLACK,
                            text_align=ft.TextAlign.LEFT),
                    padding=10,
                    height=50,
                    alignment=ft.alignment.bottom_left,
                    col={"sm": 4, "md": 8, "xl": 10}
                ),
                ft.Container(
                    tvf_accessibility,
                    width=10,
                    col={"sm": 6, "md": 4, "xl": 2}
                ),
            ],
        ),
        # BH
        ft.ResponsiveRow(
            [
                ft.Container(
                    ft.Text(value="Do you need lecture material",
                            size=sz,
                            color=ft.colors.BLACK,
                            text_align=ft.TextAlign.LEFT),
                    padding=10,
                    height=50,
                    alignment=ft.alignment.bottom_left,
                    col={"sm": 4, "md": 8, "xl": 10}
                ),
                ft.Container(
                    lecture_material,
                    width=10,
                    col={"sm": 6, "md": 4, "xl": 2}
                ),
            ],
        ),

        # BI
        ft.ResponsiveRow(
            [
                ft.Container(
                    ft.Text(value="It is difficult to convey complex concepts in online mode",
                            size=sz,
                            color=ft.colors.BLACK,
                            text_align=ft.TextAlign.LEFT),
                    padding=10,
                    height=50,
                    alignment=ft.alignment.bottom_left,
                    col={"sm": 4, "md": 8, "xl": 10}
                ),
                ft.Container(
                    conveying_concepts,
                    width=10,
                    col={"sm": 6, "md": 4, "xl": 2}
                ),
            ],
        ),
        # BK
        ft.ResponsiveRow(
            [
                ft.Container(
                    ft.Text(value="Mother's Education",
                            size=sz,
                            color=ft.colors.BLACK,
                            text_align=ft.TextAlign.LEFT),
                    padding=10,
                    height=50,
                    alignment=ft.alignment.bottom_left,
                    col={"sm": 4, "md": 8, "xl": 10}
                ),
                ft.Container(
                    mothers_education,
                    width=10,
                    col={"sm": 6, "md": 4, "xl": 2}
                ),
            ],
        ),


        b
    )

def page8(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.title = title
    page.window_width = winwidth
    page.window_height = winheight
    page.window_resizable = False

    def remarks(gpa):
        if 3.51 <= gpa <= 4.00:
            return "Extraordinary Performance"
        elif 3.00 <= gpa <= 3.50:
            return "Very Good Performance"
        elif 2.51 <= gpa <= 2.99:
            return "Good Performance"
        elif 2.00 <= gpa <= 2.50:
            return "Satisfactory  Performance"
        elif 1.00 <= gpa <= 1.99:
            return "Poor Performance"
        elif 0.00 <= gpa <= 0.99:
            return "Very Poor  Performance"


    def page4data(e):
        print(len(data))
        if len(data)<64:
            data.append(stressfulness.value)
        modelval=model1.value
        modelval = int(modelval)
        ad = 0.0
        if modelval == 0:

            loaded_model = joblib.load(f'rf_model (1).pkl')
            prediction = loaded_model.predict([data])

            for i in CGPA:
                ad += float(i)
            ad += prediction[0]
            prediction[0] = round(prediction[0], 2)
            Total_CGP = ad / 5
            Total_CGP = round(Total_CGP, 2)
            page.clean()
            page.add(
                ft.ResponsiveRow(
                    [
                        ft.Container(
                            ft.Text(value="Chose your prediction model",
                                    size=sz,
                                    color=ft.colors.BLACK,
                                    text_align=ft.TextAlign.LEFT),
                            padding=10,
                            height=50,
                            alignment=ft.alignment.bottom_left,
                            col={"sm": 4, "md": 8, "xl": 10}
                        ),
                        ft.Container(
                            model1,
                            width=10,
                            col={"sm": 6, "md": 4, "xl": 2}
                        ),
                    ],
                ),
                # BB
                ft.ResponsiveRow(
                    [
                        ft.Container(
                            ft.Text(value="SGPA in BS Fifth semester",
                                    size=sz,
                                    color=ft.colors.BLACK,
                                    text_align=ft.TextAlign.LEFT),
                            padding=10,
                            height=105,
                            alignment=ft.alignment.bottom_left,
                            col={"sm": 4, "md": 4, "xl": 10}
                        ),
                        ft.Container(
                            ft.Text(value=f"{prediction[0]}",
                                    size=sz,
                                    color=ft.colors.BLACK,
                                    text_align=ft.TextAlign.LEFT),
                            width=10,
                            height=94,
                            alignment=ft.alignment.bottom_left,
                            col={"sm": 6, "md": 4, "xl": 2}
                        ),
                    ],
                ),

                # BJ
                ft.ResponsiveRow(
                    [
                        ft.Container(
                            ft.Text(value="CGPA in BS Fifth semester",
                                    size=sz,
                                    color=ft.colors.BLACK,
                                    text_align=ft.TextAlign.LEFT),
                            padding=10,
                            height=70,
                            alignment=ft.alignment.bottom_left,
                            col={"sm": 4, "md": 4, "xl": 10}
                        ),
                        ft.Container(
                            ft.Text(value=f"{Total_CGP}",
                                    size=sz,
                                    color=ft.colors.BLACK,
                                    text_align=ft.TextAlign.LEFT),
                            width=10,
                            height=61,
                            alignment=ft.alignment.bottom_left,
                            col={"sm": 6, "md": 4, "xl": 2}
                        ),
                    ],
                ),
                ft.ResponsiveRow(
                    [
                        ft.Container(
                            ft.Text(value=f"Remarks: {remarks(float(prediction[0]))}",
                                    size=sz,
                                    color=ft.colors.BLACK,
                                    text_align=ft.TextAlign.LEFT),
                            padding=10,
                            height=70,
                            alignment=ft.alignment.bottom_left,
                            col={"sm": 5, "md": 8, "xl": 12}
                        )
                    ],
                ),

                b
            )

            page.update()
        elif modelval == 1:
            loaded_model = joblib.load(f'rf2_model (1).pkl')
            prediction = loaded_model.predict([data])
            for i in CGPA:
                ad += float(i)
            ad += prediction[0]
            prediction[0] = round(prediction[0], 2)
            Total_CGP = ad / 5
            Total_CGP = round(Total_CGP, 2)
            page.clean()
            print(prediction[0],Total_CGP)
            page.add(
                ft.ResponsiveRow(
                    [
                        ft.Container(
                            ft.Text(value="Chose your prediction model",
                                    size=sz,
                                    color=ft.colors.BLACK,
                                    text_align=ft.TextAlign.LEFT),
                            padding=10,
                            height=50,
                            alignment=ft.alignment.bottom_left,
                            col={"sm": 4, "md": 8, "xl": 10}
                        ),
                        ft.Container(
                            model1,
                            width=10,
                            col={"sm": 6, "md": 4, "xl": 2}
                        ),
                    ],
                ),
                # BB
                ft.ResponsiveRow(
                    [
                        ft.Container(
                            ft.Text(value="SGPA in BS Fifth semester",
                                    size=sz,
                                    color=ft.colors.BLACK,
                                    text_align=ft.TextAlign.LEFT),
                            padding=10,
                            height=105,
                            alignment=ft.alignment.bottom_left,
                            col={"sm": 4, "md": 4, "xl": 10}
                        ),
                        ft.Container(
                            ft.Text(value=f"{prediction[0]}",
                                    size=sz,
                                    color=ft.colors.BLACK,
                                    text_align=ft.TextAlign.LEFT),
                            width=10,
                            height=94,
                            alignment=ft.alignment.bottom_left,
                            col={"sm": 6, "md": 4, "xl": 2}
                        ),
                    ],
                ),

                # BJ
                ft.ResponsiveRow(
                    [
                        ft.Container(
                            ft.Text(value="CGPA in BS Fifth semester",
                                    size=sz,
                                    color=ft.colors.BLACK,
                                    text_align=ft.TextAlign.LEFT),
                            padding=10,
                            height=70,
                            alignment=ft.alignment.bottom_left,
                            col={"sm": 4, "md": 4, "xl": 10}
                        ),
                        ft.Container(
                            ft.Text(value=f"{Total_CGP}",
                                    size=sz,
                                    color=ft.colors.BLACK,
                                    text_align=ft.TextAlign.LEFT),
                            width=10,
                            height=61,
                            alignment=ft.alignment.bottom_left,
                            col={"sm": 6, "md": 4, "xl": 2}
                        ),
                    ],
                ),
                ft.ResponsiveRow(
                    [
                        ft.Container(
                            ft.Text(value=f"Remarks: {remarks(float(prediction[0]))}",
                                    size=sz,
                                    color=ft.colors.BLACK,
                                    text_align=ft.TextAlign.LEFT),
                            padding=10,
                            height=70,
                            alignment=ft.alignment.bottom_left,
                            col={"sm": 5, "md": 8, "xl": 12}
                        )
                    ],
                ),b
            )

            page.update()
        elif modelval == 2:
            loaded_model = joblib.load(f'gb_model (1).pkl')
            prediction = loaded_model.predict([data])
            for i in CGPA:
                ad += float(i)
            ad += prediction[0]
            prediction[0] = round(prediction[0], 2)
            Total_CGP = ad / 5
            Total_CGP = round(Total_CGP, 2)
            page.clean()
            page.add(
                ft.ResponsiveRow(
                    [
                        ft.Container(
                            ft.Text(value="Chose your prediction model",
                                    size=sz,
                                    color=ft.colors.BLACK,
                                    text_align=ft.TextAlign.LEFT),
                            padding=10,
                            height=50,
                            alignment=ft.alignment.bottom_left,
                            col={"sm": 4, "md": 8, "xl": 10}
                        ),
                        ft.Container(
                            model1,
                            width=10,
                            col={"sm": 6, "md": 4, "xl": 2}
                        ),
                    ],
                ),
                ft.ResponsiveRow(
                    [
                        ft.Container(
                            ft.Text(value="SGPA in BS Fifth semester",
                                    size=sz,
                                    color=ft.colors.BLACK,
                                    text_align=ft.TextAlign.LEFT),
                            padding=10,
                            height=105,
                            alignment=ft.alignment.bottom_left,
                            col={"sm": 4, "md": 4, "xl": 10}
                        ),
                        ft.Container(
                            ft.Text(value=f"{prediction[0]}",
                                    size=sz,
                                    color=ft.colors.BLACK,
                                    text_align=ft.TextAlign.LEFT),
                            width=10,
                            height=94,
                            alignment=ft.alignment.bottom_left,
                            col={"sm": 6, "md": 4, "xl": 2}
                        ),
                    ],
                ),

                # BJ
                ft.ResponsiveRow(
                    [
                        ft.Container(
                            ft.Text(value="CGPA in BS Fifth semester",
                                    size=sz,
                                    color=ft.colors.BLACK,
                                    text_align=ft.TextAlign.LEFT),
                            padding=10,
                            height=70,
                            alignment=ft.alignment.bottom_left,
                            col={"sm": 4, "md": 4, "xl": 10}
                        ),
                        ft.Container(
                            ft.Text(value=f"{Total_CGP}",
                                    size=sz,
                                    color=ft.colors.BLACK,
                                    text_align=ft.TextAlign.LEFT),
                            width=10,
                            height=61,
                            alignment=ft.alignment.bottom_left,
                            col={"sm": 6, "md": 4, "xl": 2}
                        ),
                    ],
                ),
                ft.ResponsiveRow(
                    [
                        ft.Container(
                            ft.Text(value=f"Remarks: {remarks(float(prediction[0]))}",
                                    size=sz,
                                    color=ft.colors.BLACK,
                                    text_align=ft.TextAlign.LEFT),
                            padding=10,
                            height=70,
                            alignment=ft.alignment.bottom_left,
                            col={"sm": 5, "md": 8, "xl": 12}
                        )
                    ],
                ),
                b
            )

            page.update()
        elif modelval == 3:
            loaded_model = joblib.load(f'ab_model (1).pkl')
            prediction = loaded_model.predict([data])
            for i in CGPA:
                ad += float(i)
            ad += prediction[0]
            prediction[0] = round(prediction[0], 2)
            Total_CGP = ad / 5
            Total_CGP = round(Total_CGP, 2)
            page.clean()

            page.add(
                ft.ResponsiveRow(
                    [
                        ft.Container(
                            ft.Text(value="Chose your prediction model",
                                    size=sz,
                                    color=ft.colors.BLACK,
                                    text_align=ft.TextAlign.LEFT),
                            padding=10,
                            height=50,
                            alignment=ft.alignment.bottom_left,
                            col={"sm": 4, "md": 8, "xl": 10}
                        ),
                        ft.Container(
                            model1,
                            width=10,
                            col={"sm": 6, "md": 4, "xl": 2}
                        ),
                    ],
                ),
                # BB
                ft.ResponsiveRow(
                    [
                        ft.Container(
                            ft.Text(value="SGPA in BS Fifth semester",
                                    size=sz,
                                    color=ft.colors.BLACK,
                                    text_align=ft.TextAlign.LEFT),
                            padding=10,
                            height=105,
                            alignment=ft.alignment.bottom_left,
                            col={"sm": 4, "md": 4, "xl": 10}
                        ),
                        ft.Container(
                            ft.Text(value=f"{prediction[0]}",
                                    size=sz,
                                    color=ft.colors.BLACK,
                                    text_align=ft.TextAlign.LEFT),
                            width=10,
                            height=94,
                            alignment=ft.alignment.bottom_left,
                            col={"sm": 6, "md": 4, "xl": 2}
                        ),
                    ],
                ),

                # BJ
                ft.ResponsiveRow(
                    [
                        ft.Container(
                            ft.Text(value="CGPA in BS Fifth semester",
                                    size=sz,
                                    color=ft.colors.BLACK,
                                    text_align=ft.TextAlign.LEFT),
                            padding=10,
                            height=70,
                            alignment=ft.alignment.bottom_left,
                            col={"sm": 4, "md": 4, "xl": 10}
                        ),
                        ft.Container(
                            ft.Text(value=f"{Total_CGP}",
                                    size=sz,
                                    color=ft.colors.BLACK,
                                    text_align=ft.TextAlign.LEFT),
                            width=10,
                            height=61,
                            alignment=ft.alignment.bottom_left,
                            col={"sm": 6, "md": 4, "xl": 2}
                        ),
                    ],
                ),
                ft.ResponsiveRow(
                    [
                        ft.Container(
                            ft.Text(value=f"Remarks: {remarks(float(prediction[0]))}",
                                    size=sz,
                                    color=ft.colors.BLACK,
                                    text_align=ft.TextAlign.LEFT),
                            padding=10,
                            height=70,
                            alignment=ft.alignment.bottom_left,
                            col={"sm": 5, "md": 8, "xl": 12}
                        )
                    ],
                ),
                b
            )

            page.update()
        elif modelval == 4:
            loaded_model = joblib.load(f'bg_model (1).pkl')
            prediction = loaded_model.predict([data])
            for i in CGPA:
                ad += float(i)
            ad += prediction[0]
            prediction[0] = round(prediction[0], 2)
            Total_CGP = ad / 5
            Total_CGP = round(Total_CGP, 2)
            page.clean()
            page.add(
                ft.ResponsiveRow(
                    [
                        ft.Container(
                            ft.Text(value="Chose your prediction model",
                                    size=sz,
                                    color=ft.colors.BLACK,
                                    text_align=ft.TextAlign.LEFT),
                            padding=10,
                            height=50,
                            alignment=ft.alignment.bottom_left,
                            col={"sm": 4, "md": 8, "xl": 10}
                        ),
                        ft.Container(
                            model1,
                            width=10,
                            col={"sm": 6, "md": 4, "xl": 2}
                        ),
                    ],
                ),
                # BB
                ft.ResponsiveRow(
                    [
                        ft.Container(
                            ft.Text(value="SGPA in BS Fifth semester",
                                    size=sz,
                                    color=ft.colors.BLACK,
                                    text_align=ft.TextAlign.LEFT),
                            padding=10,
                            height=105,
                            alignment=ft.alignment.bottom_left,
                            col={"sm": 4, "md": 4, "xl": 10}
                        ),
                        ft.Container(
                            ft.Text(value=f"{prediction[0]}",
                                    size=sz,
                                    color=ft.colors.BLACK,
                                    text_align=ft.TextAlign.LEFT),
                            width=10,
                            height=94,
                            alignment=ft.alignment.bottom_left,
                            col={"sm": 6, "md": 4, "xl": 2}
                        ),
                    ],
                ),

                # BJ
                ft.ResponsiveRow(
                    [
                        ft.Container(
                            ft.Text(value="CGPA in BS Fifth semester",
                                    size=sz,
                                    color=ft.colors.BLACK,
                                    text_align=ft.TextAlign.LEFT),
                            padding=10,
                            height=70,
                            alignment=ft.alignment.bottom_left,
                            col={"sm": 4, "md": 4, "xl": 10}
                        ),
                        ft.Container(
                            ft.Text(value=f"{Total_CGP}",
                                    size=sz,
                                    color=ft.colors.BLACK,
                                    text_align=ft.TextAlign.LEFT),
                            width=10,
                            height=61,
                            alignment=ft.alignment.bottom_left,
                            col={"sm": 6, "md": 4, "xl": 2}
                        ),
                    ],
                ),
                ft.ResponsiveRow(
                    [
                        ft.Container(
                            ft.Text(value=f"Remarks: {remarks(float(prediction[0]))}",
                                    size=sz,
                                    color=ft.colors.BLACK,
                                    text_align=ft.TextAlign.LEFT),
                            padding=10,
                            height=70,
                            alignment=ft.alignment.bottom_left,
                            col={"sm": 5, "md": 8, "xl": 12}
                        )
                    ],
                ),
                b
            )

            page.update()
        elif modelval == 5:
            loaded_model = joblib.load(f'ensemble_model (1).pkl')
            prediction = loaded_model.predict([data])
            for i in CGPA:
                ad += float(i)
            ad += prediction[0]
            prediction[0] = round(prediction[0], 2)
            Total_CGP = ad / 5
            Total_CGP = round(Total_CGP, 2)
            page.clean()
            page.add(
                ft.ResponsiveRow(
                    [
                        ft.Container(
                            ft.Text(value="Chose your prediction model",
                                    size=sz,
                                    color=ft.colors.BLACK,
                                    text_align=ft.TextAlign.LEFT),
                            padding=10,
                            height=50,
                            alignment=ft.alignment.bottom_left,
                            col={"sm": 4, "md": 8, "xl": 10}
                        ),
                        ft.Container(
                            model1,
                            width=10,
                            col={"sm": 6, "md": 4, "xl": 2}
                        ),
                    ],
                ),
                ft.ResponsiveRow(
                    [
                        ft.Container(
                            ft.Text(value="SGPA in BS Fifth semester",
                                    size=sz,
                                    color=ft.colors.BLACK,
                                    text_align=ft.TextAlign.LEFT),
                            padding=10,
                            height=105,
                            alignment=ft.alignment.bottom_left,
                            col={"sm": 4, "md": 4, "xl": 10}
                        ),
                        ft.Container(
                            ft.Text(value=f"{prediction[0]}",
                                    size=sz,
                                    color=ft.colors.BLACK,
                                    text_align=ft.TextAlign.LEFT),
                            width=10,
                            height=94,
                            alignment=ft.alignment.bottom_left,
                            col={"sm": 6, "md": 4, "xl": 2}
                        ),
                    ],
                ),


                ft.ResponsiveRow(
                    [
                        ft.Container(
                            ft.Text(value="CGPA in BS Fifth semester",
                                    size=sz,
                                    color=ft.colors.BLACK,
                                    text_align=ft.TextAlign.LEFT),
                            padding=10,
                            height=70,
                            alignment=ft.alignment.bottom_left,
                            col={"sm": 4, "md": 4, "xl": 10}
                        ),
                        ft.Container(
                            ft.Text(value=f"{Total_CGP}",
                                    size=sz,
                                    color=ft.colors.BLACK,
                                    text_align=ft.TextAlign.LEFT),
                            width=10,
                            height=61,
                            alignment=ft.alignment.bottom_left,
                            col={"sm": 6, "md": 4, "xl": 2}
                        ),
                    ],
                ),
                ft.ResponsiveRow(
                    [
                        ft.Container(
                            ft.Text(value=f"Remarks: {remarks(float(prediction[0]))}",
                                    size=sz,
                                    color=ft.colors.BLACK,
                                    text_align=ft.TextAlign.LEFT),
                            padding=10,
                            height=70,
                            alignment=ft.alignment.bottom_left,
                            col={"sm": 5, "md": 8, "xl": 12}
                        )
                    ],
                ),
                b
            )

            page.update()






    b = ft.ElevatedButton("Predict", on_click=page4data, width=150, height=60)
    # drop down

    # drop down
    stressfulness = ft.Dropdown(
        width=40,
        options=[
            ft.dropdown.Option(value, key) for key, value in
            dictionary.unannounced_quizzes_stressfulness_encoding.items()
        ],
        value=1)

    model1 = ft.Dropdown(
        width=40,
        options=[
            ft.dropdown.Option(value, key) for key, value in
            dictionary.model.items()
        ],
        value=0)

    page.add(
        # BB
        ft.ResponsiveRow(
            [
                ft.Container(
                    ft.Text(value="Un-announced quizzes are a form of torture and "
                                  "have negative impact on learning environment.",
                            size=sz,
                            color=ft.colors.BLACK,
                            text_align=ft.TextAlign.LEFT),
                    padding=10,
                    height=70,
                    alignment=ft.alignment.bottom_left,
                    col={"sm": 4, "md": 8, "xl": 10}
                ),
                ft.Container(
                    stressfulness,
                    width=10,
                    col={"sm": 6, "md": 4, "xl": 2}
                ),
            ],
        ),

        # BJ
        ft.ResponsiveRow(
            [
                ft.Container(
                    ft.Text(value="Chose your prediction model",
                            size=sz,
                            color=ft.colors.BLACK,
                            text_align=ft.TextAlign.LEFT),
                    padding=10,
                    height=50,
                    alignment=ft.alignment.bottom_left,
                    col={"sm": 4, "md": 8, "xl": 10}
                ),
                ft.Container(
                    model1,
                    width=10,
                    col={"sm": 6, "md": 4, "xl": 2}
                ),
            ],
        ),
        b
    )



ft.app(target=page1)