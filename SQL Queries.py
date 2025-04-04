import streamlit as st
import pandas as pd
import sqlite3

# Database Connection (Replace 'your_database.db' with your actual database file)
def create_connection():
    conn = None
    try:
        conn = sqlite3.connect('food_wastage.db')
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
    return conn

# SQL Query Functions
def execute_query(conn, query):
    try:
        df = pd.read_sql_query(query, conn)
        return df
    except Exception as e:
        st.error(f"Error executing query: {e}")
        return None

def contact_button():
    return st.selectbox("City",
['Adambury','Adamsview','Adamsville','Aguirreville','Alexanderchester','Alexanderstad','Allenborough','Allenton','Amandaborough','Amandashire','Amberton','Ambertown','Amyport','Andersonmouth','Andersonville','Andreaborough','Andrewsmouth','Andrewstad','Anitashire','Annahaven','Annetteburgh','Anneville','Anthonyborough','Anthonychester','Anthonyfort','Anthonyhaven','Anthonyshire','Anthonyton','Aprilberg','Arnoldmouth','Ashleyhaven','Ashleyton','Bairdfort','Baldwinshire','Barkerborough','Barryside','Bartonborough','Basstown','Batesstad','Beasleyhaven','Belindaville','Bellport','Benjaminstad','Bentleyburgh','Bentonfurt','Blaketown','Bonillahaven','Boylechester','Bradleyborough','Bradleyport','Bradleyview','Brandyberg','Brendantown','Brennanstad','Brewerfort','Brianside','Bridgetside','Brittanyland','Brittanyport','Brittanyside','Brittanyville','Brookeland','Brownberg','Brownchester','Browninghaven','Brownshire','Brownton','Browntown','Bryantton','Butlerview','Cabreraberg','Callahanside','Cameronside','Campbellbury','Campbellchester','Cannonside','Carlborough','Carlbury','Carolchester','Carrport','Cassandraville','Castilloport','Chadview','Chambersfort','Charlesland','Charlesmouth','Charlesview','Chelseaside','Chelseyfort','Christianfurt','Christinaland','Christinamouth','Christinetown','Christopherchester','Christopherside','Christopherstad','Christopherton','Cindyshire','Cisnerostown','Clarkberg','Codyview','Coleburgh','Colemanton','Collinsmouth','Collinston','Connieside','Contrerasberg','Coopermouth','Copelandchester','Cordovaborough','Courtneychester','Crystalborough','Cummingstown','Cunninghambury','Danachester','Danaville','Dannybury','Darrellfurt','Darrylchester','Davidborough','Davidchester','Davidland','Davidport','Davidville','Davisshire','Davisview','Deanport','Deborahfurt','Deborahland','Deckermouth','Derekland','Derekport','Derekshire','Devinmouth','Devinton','Donnaborough','Drakeville','Durhamchester','East Aaron','East Alexisberg','East Amyfurt','East Amymouth','East Andrea','East Andrewland','East Angela','East Angelafort','East Annshire','East Anthony','East Ashleyshire','East Austin','East Benjaminland','East Bernard','East Brittanyland','East Candace','East Caseyfort','East Christophertown','East Courtneymouth','East Craig','East Cynthia','East Darrell','East Deborah','East Deniseborough','East Donnafort','East Edwinburgh','East Elizabeth','East Elizabethberg','East Emily','East Emilyburgh','East Garyton','East Heather','East Heatherport','East Jacobchester','East Janet','East Jennifer','East Jesse','East John','East Johnburgh','East Joseph','East Kevin','East Kimberly','East Laura','East Laurashire','East Lauren','East Lindsayville','East Lisa','East Lori','East Meganfort','East Melissa','East Michael','East Michelle','East Nicholasbury','East Phillipton','East Richardside','East Robert','East Roberthaven','East Robertton','East Rossside','East Samantha','East Sandra','East Sandratown','East Shanestad','East Sheena','East Sonyaport','East Stephanie','East Stephanieview','East Tammy','East Terrancemouth','East Timothy','East Williamburgh','East Williamshire','Edwardsbury','Elliottberg','Ericfort','Erikatown','Estradafort','Evansmouth','Fisherstad','Flemingport','Floresville','Fowlerbury','Francisshire','Frederickside','Frostberg','Fullerborough','Gaineschester','Galvanfurt','Garciaberg','Garciamouth','Garciaport','Garciaside','Garciatown','Gardnerfort','Garzaville','Gibsonfort','Ginaview','Gomezfurt','Gonzalesport','Grahamside','Gutierrezshire','Hamiltontown','Harrishaven','Harrisonbury','Hawkinsmouth','Hayesville','Heathborough','Heathermouth','Heatherside','Heatherview','Henrychester','Herbertbury','Hestermouth','Hillburgh','Hollyhaven','Holtmouth','Huberstad','Huntermouth','Jameschester','Jamesfurt','Jamesport','Jamesview','Jamesville','Janetborough','Jasmineberg','Jasminechester','Jasonland','Jasonmouth','Jasonstad','Jefferyside','Jeffreyburgh','Jeffreybury','Jeffreyport','Jeffreyshire','Jennifertown','Jenniferview','Jenniferville','Jeremiahfort','Jessestad','Jessicaland','Jimmyberg','Jimmymouth','Johnport','Johnsonborough','Johnsonside','Johnstonhaven','Johnton','Jonathanhaven','Jonathanmouth','Jonathanstad','Joneshaven','Jonesport','Jonestown','Jordanberg','Jordanborough','Jordanhaven','Josephburgh','Joseville','Joshuastad','Judystad','Justinhaven','Kaitlynville','Karentown','Katherineborough','Katherinefurt','Kayleefort','Keithburgh','Kellyberg','Kellytown','Kennedychester','Kentland','Kevinfort','Kimberlychester','Kylehaven','Lake Alexis','Lake Alicia','Lake Allen','Lake Amymouth','Lake Andrewmouth','Lake Anthonyport','Lake April','Lake Benjamin','Lake Bianca','Lake Brendaland','Lake Carlos','Lake Cathy','Lake Charleston','Lake Cheryl','Lake Chloeshire','Lake Christinaborough','Lake Christopherburgh','Lake Christophermouth','Lake Coryhaven','Lake Deborah','Lake Dennischester','Lake Devon','Lake Diane','Lake Donaldchester','Lake Donaldmouth','Lake Donna','Lake Ethanview','Lake Gary','Lake George','Lake Heather','Lake Jaclyn','Lake James','Lake Jamestown','Lake Jasmin','Lake Jason','Lake Jefferyborough','Lake Jeffreytown','Lake Jessicamouth','Lake Jesusview','Lake Joelshire','Lake Joseph','Lake Josephton','Lake Justin','Lake Karenfurt','Lake Kari','Lake Katherinechester','Lake Kelly','Lake Kendramouth','Lake Kristentown','Lake Kyle','Lake Larry','Lake Latasha','Lake Lauraton','Lake Lauren','Lake Lindsay','Lake Lindsey','Lake Lisa','Lake Lorrainefort','Lake Maria','Lake Michael','Lake Michaelchester','Lake Michaelfurt','Lake Michaelview','Lake Mistyton','Lake Monique','Lake Nathan','Lake Nicolebury','Lake Rachael','Lake Raymondton','Lake Regina','Lake Richardhaven','Lake Ryanbury','Lake Sarah','Lake Shelby','Lake Stephen','Lake Tamara','Lake Theresa','Lake Traceyburgh','Lake Travis','Lake Vanessa','Lake Vanessaland','Lake Xavierburgh','Lamberttown','Latoyaberg','Laurietown','Leeburgh','Leonardborough','Leonfort','Leslieville','Lesterstad','Leville','Levytown','Lewisberg','Lewishaven','Liberg','Linchester','Lindseybury','Lindseyland','Lisaborough','Lisafort','Lisamouth','Longland','Lopezmouth','Lopezport','Louismouth','Lucasmouth','Madelinechester','Madisonfort','Manningshire','Manuelhaven','Marcstad','Marissaville','Markberg','Markborough','Markport','Marthaside','Martinezfort','Martinville','Marymouth','Matthewbury','Maxwellburgh','Maynardstad','Maysside','Mcclainfurt','Mckinneymouth','Medinatown','Meganshire','Meghanfurt','Mendezmouth','Mendozastad','Meyersland','Michaelport','Michaelton','Michaelview','Michellechester','Mikaylachester','Millerstad','Millerview','Mitchellmouth','Mooneybury','Mooremouth','Mooreview','Moralesberg','Moralesside','Morganhaven','Morganside','Morriston','Mortonfort','Moseshaven','Muellermouth','Murphyberg','Murrayborough','Myerschester','Nathanielbury','New Aaronberg','New Amanda','New Baileyfort','New Billy','New Bobbytown','New Calebberg','New Carol','New Connorfort','New Crystal','New Curtis','New Daniel','New David','New Dawnborough','New Denise','New Douglas','New Emily','New Erica','New Evanport','New Frank','New Ginaborough','New Hannah','New Heidi','New Hollyfurt','New Jacob','New Jamesburgh','New Jason','New Jenniferbury','New Jeremyberg','New Jessica','New Joel','New John','New Johnfurt','New Josemouth','New Joshuamouth','New Kevintown','New Larry','New Leslieport','New Lisa','New Matthew','New Michaelmouth','New Michelle','New Monicaside','New Natasha','New Ninashire','New Rachel','New Rhonda','New Richard','New Ricky','New Robert','New Robertland','New Robertstad','New Rodneyville','New Ryanbury','New Samuel','New Steven','New Tammyland','New Thomasmouth','New Tiffanystad','New Travisshire','New Wendymouth','New William','New Willieburgh','New Zachary','Nicolefort','Nicoletown','Nolanmouth','North Aaron','North Alison','North Amanda','North Amber','North Ashley','North Bethanyville','North Biancaview','North Brendaborough','North Brentbury','North Briannabury','North Brooke','North Caitlin','North Carmen','North Carolfurt','North Catherine','North Charlesside','North Chase','North Christina','North Crystal','North Destiny','North Douglasfurt','North Ebony','North Edwinchester','North Elizabeth','North Gary','North Garybury','North Ianbury','North James','North Jamesberg','North Jenniferport','North Joseph','North Julieburgh','North Katelyn','North Katelynland','North Katherineshire','North Keith','North Kennethshire','North Kennethview','North Kevinhaven','North Kylestad','North Lauren','North Lindseychester','North Lisaland','North Lisamouth','North Mariahchester','North Marthaton','North Mary','North Melanie','North Michelle','North Mike','North Nathan','North Nicholas','North Nicoleport','North Paulstad','North Ravenfurt','North Richard','North Ronaldburgh','North Ronaldmouth','North Ryan','North Sharonberg','North Sharonburgh','North Sherrimouth','North Stephanieville','North Steven','North Stevenbury','North Susan','North Tom','North Tracy','North Valerie','North Victoriastad','North William','Olsenstad','Owenschester','Owensstad','Padillamouth','Padillatown','Pamelaberg','Pamelaburgh','Parksburgh','Patrickfort','Patrickmouth','Paulmouth','Pearsonchester','Penabury','Perezport','Pereztown','Perkinsbury','Peterhaven','Petersonburgh','Petersonside','Phillipsfort','Phillipsmouth','Port Aaron','Port Allisonland','Port Amandamouth','Port Andre','Port Andrea','Port Anita','Port Brett','Port Bryce','Port Carrie','Port Christina','Port Christopher','Port Connie','Port Corystad','Port Daniel','Port Daniellechester','Port David','Port Davidshire','Port Dianaberg','Port Donnamouth','Port Donnaton','Port Dustin','Port Emily','Port Emilyburgh','Port Eric','Port Erin','Port Erinton','Port Glendastad','Port Gregton','Port Hannah','Port Hannahmouth','Port Heidiland','Port Jacob','Port Jeffrey','Port Jennifer','Port Jerome','Port Jillian','Port John','Port Julia','Port Juliafort','Port Karen','Port Kathleen','Port Kendraborough','Port Kevinburgh','Port Lance','Port Lauraville','Port Lauriechester','Port Leahfurt','Port Lesliebury','Port Linda','Port Lisamouth','Port Loganberg','Port Manuel','Port Marcland','Port Mariefort','Port Marissachester','Port Markview','Port Matthew','Port Melanie','Port Melissa','Port Michael','Port Michaelshire','Port Pamelaport','Port Patrick','Port Peter','Port Raymondburgh','Port Rebekah','Port Richardshire','Port Robert','Port Robertport','Port Robin','Port Ronaldshire','Port Rubenville','Port Staceymouth','Port Tanyaburgh','Port Timothystad','Port Troychester','Port Victoria','Priceland','Ramosville','Ramseyfort','Randallchester','Randallville','Raybury','Raymondview','Rebeccaburgh','Rebeccabury','Reidland','Reyesshire','Reynoldsbury','Riceshire','Richardfort','Richardmouth','Richardsonhaven','Richardton','Richchester','Richton','Ritterburgh','Roachhaven','Robertland','Robertschester','Robertshire','Robertsonfort','Robertton','Robinsonfort','Rodneystad','Rodriguezfurt','Rodriguezview','Rogersmouth','Roystad','Ruizmouth','Russellfurt','Salastown','Salinasville','Samanthabury','Samueltown','Samuelville','Sandersshire','Sandrastad','Saraburgh','Sarahland','Sarahside','Sarahview','Scottchester','Scotthaven','Scottton','Shannonside','Sharonton','Shawnborough','Sheenashire','Sheilaburgh','Shirleyland','Shortfurt','Smithfort','Smithmouth','Smithstad','Snyderton','Solisburgh','South Alicia','South Allison','South Allisonburgh','South Andrew','South Andrewport','South Anne','South Bradleyburgh','South Brandiberg','South Brenda','South Bryan','South Cassandra','South Charles','South Christopherborough','South Crystalberg','South Danielle','South Davidside','South Donald','South Douglashaven','South Edwardtown','South Jacobport','South Jasmineville','South Jason','South Jeffery','South Jeffrey','South Jeffreyburgh','South Jerryside','South Jessicachester','South Jillshire','South Johnshire','South Joshua','South Justinborough','South Karen','South Kathryn','South Kayla','South Kelly','South Kellyberg','South Kellyland','South Kellyville','South Kendra','South Kevinhaven','South Linda','South Lisaberg','South Lisabury','South Louis','South Marthahaven','South Melanieshire','South Michaelberg','South Michaelhaven','South Michellechester','South Morganfurt','South Nicholasville','South Nicole','South Randy','South Richard','South Richardhaven','South Robert','South Russelltown','South Sarahville','South Sarastad','South Stefanietown','South Tammy','South Thomas','South Thomasville','South Tiffanyfort','South Tina','South Tylerstad','South William','South Zacharymouth','Spenceland','Steeleport','Stephanieberg','Stevenchester','Stevensborough','Steventown','Steveport','Stewartfurt','Strongmouth','Suzanneport','Sylviabury','Tamaraside','Tammyside','Tammystad','Taylorchester','Taylorfort','Taylormouth','Thomasfurt','Thomasville','Thorntonbury','Timothychester','Timothyview','Tinamouth','Toddberg','Toddstad','Torresfort','Torresshire','Tracyfort','Tylerburgh','Tylerton','Tyronebury','Valdezborough','Valentineside','Valenzuelaville','Vazquezland','Vazquezshire','Velazquezview','Villaborough','Villastad','Wadeville','Walkerfurt','Walterborough','Walterton','Wardton','Washingtonville','Watsonstad','Watsonton','Weberfurt','West Abigailtown','West Adam','West Adammouth','West Aliciabury','West Amanda','West Amandafurt','West Anthonymouth','West Ashleytown','West Benjamin','West Billborough','West Brandon','West Carolyn','West Catherine','West Charlesborough','West Cherylfort','West Christopher','West Corey','West Daniel','West Danielborough','West Danieltown','West Dannyland','West Dawn','West Elizabethport','West Erinport','West Hunter','West James','West Jeffreyland','West Juliabury','West Julianburgh','West Kara','West Karen','West Kelli','West Kenneth','West Kevin','West Larry','West Lauraborough','West Lisamouth','West Lucasville','West Margaretfort','West Matthew','West Melissa','West Melissastad','West Miaside','West Michael','West Omar','West Omarside','West Pamelaborough','West Peter','West Peterborough','West Phillip','West Robert','West Samantha','West Samuelfurt','West Sharonview','West Stephaniemouth','West Stephen','West Stephenside','West Stevenport','West Tammy','West Theresaberg','West Thomas','West Tinamouth','West Trevorview','West Tylerberg','West Vanessafort','West Whitneymouth','Westbury','Westmouth','Wheelermouth','Williamland','Williammouth','Williamschester','Williamsfort','Williamsland','Williamsmouth','Williamsonmouth','Williamsshire','Williamview','Wilsonport','Wilsonview','Woodport','Wrightville','Yatesside','Youngchester','Zimmermanton','Zimmermanville'])

# Streamlit App
def main():
    st.title("Food Wastage Management System - SQL Queries")

    conn = create_connection()
    if conn is None:
        st.error("Failed to connect to the database. Please check your database file.")
        return

    query_options = [
        "How many food providers and receivers are there in each city?",
        "Which type of food provider contributes the most food?",
        "What is the contact information of food providers in a specific city?",
        "Which receivers have claimed the most food?",
        "What is the total quantity of food available from all providers?",
        "Which city has the highest number of food listings?",
        "What are the most commonly available food types?",
        "Which food listings are expiring soon (within the next 3 days)?",
        "How many food claims have been made for each food item?",
        "Which provider has had the highest number of successful food claims?",
        "Which city has the fastest claim rate?",
        "What percentage of food claims are completed vs. pending vs. canceled?",
        "What is the average quantity of food claimed per receiver?",
        "Which meal type is claimed the most?",
        "What is the total quantity of food donated by each provider?"
    ]

    selected_query = st.selectbox("Select a Query", query_options)

    if selected_query == query_options[2]:
        city_input = contact_button()
        if st.button("Execute Query", disabled=city_input is None): # Disable if city_input is None
            if city_input is not None:
                query = f"SELECT Name, Contact FROM Providers WHERE City = '{city_input}';"
                df = execute_query(conn, query)
                if df is not None:
                    st.dataframe(df)
    else:
        if st.button("Execute Query"):
            if selected_query == query_options[0]:
                providers_query = """SELECT
                                    lower(COALESCE(p.City, r.City)) AS city,
                                    COUNT(p.Provider_ID) AS providers_count,
                                    COUNT(r.Receiver_ID) AS receivers_count
                                FROM
                                    Providers p
                                FULL OUTER JOIN
                                    Receivers r ON lower(p.City) = lower(r.City)
                                GROUP BY
                                    lower(COALESCE(p.City, r.City));"""
                # receivers_query = "SELECT City, COUNT(Receiver_ID) AS Receiver_Count FROM Receivers GROUP BY City;"
                providers_df = execute_query(conn, providers_query)
                if providers_df is not None :
                # and receivers_df is not None:
                    st.subheader("Providers and Receivers per City:")
                    st.dataframe(providers_df)
            
            elif selected_query == query_options[1]:
                query = "SELECT Provider_Type, SUM(Quantity) AS Total_Quantity_Contributed FROM food_listings_data GROUP BY Provider_Type ORDER BY Total_Quantity_Contributed DESC LIMIT 1;"
                df = execute_query(conn, query)
                if df is not None:
                    st.dataframe(df)


            elif selected_query == query_options[3]:
                query = "SELECT r.Name, COUNT(c.Receiver_ID) AS Claim_Count FROM Claims c JOIN Receivers r ON c.Receiver_ID = r.Receiver_ID GROUP BY c.Receiver_ID ORDER BY Claim_Count DESC;"
                df = execute_query(conn, query)
                if df is not None:
                    st.dataframe(df)

            elif selected_query == query_options[4]:
                query = "SELECT SUM(Quantity) AS Total_Quantity FROM food_listings_data;"
                df = execute_query(conn, query)
                if df is not None:
                    st.dataframe(df)

            elif selected_query == query_options[5]:
                query = "SELECT Location, COUNT(Food_ID) AS Listing_Count FROM food_listings_data GROUP BY Location ORDER BY Listing_Count DESC LIMIT 1;"
                df = execute_query(conn, query)
                if df is not None:
                    st.dataframe(df)

            elif selected_query == query_options[6]:
                query = "SELECT Food_Type, COUNT(Food_ID) AS Food_Type_Count FROM food_listings_data GROUP BY Food_Type ORDER BY Food_Type_Count DESC;"
                df = execute_query(conn, query)
                if df is not None:
                    st.dataframe(df)

            elif selected_query == query_options[7]:
                query = "SELECT * FROM food_listings_data WHERE Expiry_Date between DATE('2024-04-03', '-1 month') and Date('now');"
                df = execute_query(conn, query)
                if df is not None:
                    st.dataframe(df)

            elif selected_query == query_options[8]:
                query = "SELECT Food_ID, COUNT(Claim_ID) AS Claim_Count FROM Claims GROUP BY Food_ID;"
                df = execute_query(conn, query)
                if df is not None:
                    st.dataframe(df)

            elif selected_query == query_options[9]:
                query = "SELECT p.Name, COUNT(c.Claim_ID) AS Successful_Claim_Count FROM Claims c JOIN Food_Listings_data fl ON c.Food_ID = fl.Food_ID JOIN Providers p ON fl.Provider_ID = p.Provider_ID WHERE c.Status = 'Completed' GROUP BY p.Provider_ID ORDER BY Successful_Claim_Count DESC LIMIT 1;"
                df = execute_query(conn, query)
                if df is not None:
                    st.dataframe(df)

            elif selected_query == query_options[10]:
                query = "SELECT fl.Location, AVG(JULIANDAY(c.Timestamp) - JULIANDAY(fl.Expiry_Date)) AS Average_Claim_Time FROM Claims c JOIN Food_Listings_data fl ON c.Food_ID = fl.Food_ID GROUP BY fl.Location ORDER BY Average_Claim_Time ASC;"
                df = execute_query(conn, query)
                if df is not None:
                    st.dataframe(df)

            elif selected_query == query_options[11]:
                query = "SELECT Status, (COUNT(*) * 100.0 / (SELECT COUNT(*) FROM Claims)) AS Percentage FROM Claims GROUP BY Status;"
                df = execute_query(conn, query)
                if df is not None:
                    st.dataframe(df)

            elif selected_query == query_options[12]:
                query = "SELECT AVG(fl.Quantity) AS Average_Quantity_Claimed FROM Food_Listings_data fl JOIN Claims c ON fl.Food_ID = c.Food_ID;"
                df = execute_query(conn, query)
                if df is not None:
                    st.dataframe(df)

            elif selected_query == query_options[13]:
                query = "SELECT Meal_Type, COUNT(c.Claim_ID) AS Claim_Count FROM Claims c JOIN Food_Listings_data fl ON c.Food_ID = fl.Food_ID GROUP BY Meal_Type ORDER BY Claim_Count DESC LIMIT 1;"
                df = execute_query(conn, query)
                if df is not None:
                    st.dataframe(df)

            elif selected_query == query_options[14]:
                query = "SELECT p.Name, SUM(fl.Quantity) AS Total_Quantity_Donated FROM Food_Listings_data fl JOIN Providers p ON fl.Provider_ID = p.Provider_ID GROUP BY p.Provider_ID;"
                df = execute_query(conn, query)
                if df is not None:
                    st.dataframe(df)

    if conn is not None:
        conn.close()

if __name__ == "__main__":
    main()