<template>
  <div class="middle">
    <SideNav @changeLibrarianView="changeMiddleView" page="librarian" />

    <div class="mainPanel" v-if="changeView == 1">
      <div class="statistics">
        <div class="dashTabsContainer">
          <div
            :class="`dashTab ${statsTab == 1 ? 'currentDashTab' : ''}`"
            @click="changeStatsTab(1)"
          >
            Users Statistics
          </div>
          <div
            :class="`dashTab ${statsTab == 2 ? 'currentDashTab' : ''}`"
            @click="changeStatsTab(2)"
          >
            Books Statistics
          </div>
          <div
            :class="`dashTab ${statsTab == 3 ? 'currentDashTab' : ''}`"
            @click="changeStatsTab(3)"
          >
            Authors Statistics
          </div>
        </div>
        <div class="coreStatistics" v-if="statsTab == 1">
          <div class="dashRow">
            <div class="userBarChart">
              <BarChartView
                :barData="userStatsData.barData"
                class="chartView"
              />
            </div>
            <div class="userDataValues">
              <DataCards
                cardHead="Total Users"
                :cardValue="userStatsData.dataValues.total_users"
                fontSize="2.5rem"
                cardWidth="14rem"
                cardHeight="8rem"
              />
              <DataCards
                cardHead="Active Users"
                :cardValue="userStatsData.dataValues.total_active_users"
                fontSize="2.5rem"
                cardWidth="14rem"
                cardHeight="8rem"
              />
              <DataCards
                cardHead="Most Active User"
                :cardValue="userStatsData.dataValues.most_active_user"
                fontSize="2rem"
                cardWidth="14rem"
                cardHeight="8rem"
              />
              <DataCards
                cardHead="# Banned Users"
                :cardValue="userStatsData.dataValues.banned_users"
                fontSize="2.5rem"
                cardWidth="14rem"
                cardHeight="8rem"
              />
            </div>
          </div>
          <div class="dashRow">
            <div class="leagueStats">
              <div class="leagueStatsHead">User League Distribution</div>
              <div class="leagueDivCont">
                <div class="leagueDiv">
                  <p class="leagueName">No League</p>
                  <div class="leagueLogoCont"></div>
                  <p class="leagueStat">{{ userStatsData.userLeague.No }}</p>
                </div>
                <div class="leagueDiv">
                  <p class="leagueName">Reader League</p>
                  <div class="leagueLogoCont">
                    <img
                      src="@/assets/images/Reader_logo.png"
                      alt="Reader logo"
                      class="leagueLogo"
                    />
                  </div>
                  <p class="leagueStat">
                    {{ userStatsData.userLeague.Reader }}
                  </p>
                </div>
                <div class="leagueDiv">
                  <p class="leagueName">Literati League</p>
                  <div class="leagueLogoCont">
                    <img
                      src="@/assets/images/Literati_logo.png"
                      alt="Literati logo"
                      class="leagueLogo"
                    />
                  </div>
                  <p class="leagueStat">
                    {{ userStatsData.userLeague.Literati }}
                  </p>
                </div>
                <div class="leagueDiv">
                  <p class="leagueName">Scholar League</p>
                  <div class="leagueLogoCont">
                    <img
                      src="@/assets/images/Scholar_logo.png"
                      alt="Scholar logo"
                      class="leagueLogo"
                    />
                  </div>
                  <p class="leagueStat">
                    {{ userStatsData.userLeague.Scholar }}
                  </p>
                </div>
                <div class="leagueDiv">
                  <p class="leagueName">Sage League</p>
                  <div class="leagueLogoCont">
                    <img
                      src="@/assets/images/Sage_logo.png"
                      alt=""
                      class="leagueLogo"
                    />
                  </div>
                  <p class="leagueStat">{{ userStatsData.userLeague.Sage }}</p>
                </div>
              </div>
            </div>
            <div class="userGenders">
              <PieChartView
                style="margin-right: 2rem"
                :pieData="userStatsData.pieData"
                class="chartView"
              />
            </div>
          </div>
        </div>
        <LibrarianBooksStats
          :bookStatsData="bookStatsData"
          v-if="statsTab == 2"
        />
        <LibrarianAuthorsStats
          :authorsStatsData="authorsStatsData"
          v-if="statsTab == 3"
        />
      </div>
    </div>
    <div class="mainPanel withPreview" v-if="changeView == 2">
      <div class="searchCont">
        <div class="searchbox">
          <input
            type="text"
            class="search"
            @change="bookSearcher()"
            id="searchbox"
            placeholder="Enter your search keyword"
          />
        </div>
      </div>

      <div class="headBookTitleContainer" v-if="searchBooks.titles.length > 0">
        <div class="headBookTitle">Search by Titles</div>
      </div>
      <div
        v-for="(book, index) in searchBooks.titles"
        :key="index"
        class="card myCard"
      >
        <div class="bookImgContainer">
          <img :src="book.img" alt="" class="bookImg" />
        </div>
        <div class="bookContent">
          <p class="bookTitle">{{ shortenText(book.book_name) }}</p>
          <p class="bookAuthor">
            AUTHOR: <span>{{ book.author_name }}</span>
          </p>
          <p class="bookAuthor">
            GENRE: <span>{{ book.genre }}</span>
          </p>
        </div>
        <div class="actions">
          <div
            class="actionBtns"
            @click="confirmDelete(book.book_id, book.book_name)"
          >
            <img
              src="@/assets/images/delete-icon.png"
              alt=""
              class="actionBtnImg"
            />
            Delete
          </div>
          <div
            class="actionBtns sideBtn"
            @click="changePreviewBook(book.book_id)"
          >
            <img
              src="@/assets/images/edit-icon.png"
              alt=""
              class="actionBtnImg"
            />
            Edit
          </div>
        </div>
      </div>
      <div class="headBookTitleContainer" v-if="searchBooks.authors.length > 0">
        <div class="headBookTitle">Search by Authors</div>
      </div>
      <div
        v-for="(book, index) in searchBooks.authors"
        :key="index"
        class="card myCard"
      >
        <div class="bookImgContainer">
          <img :src="book.img" alt="" class="bookImg" />
        </div>
        <div class="bookContent">
          <p class="bookTitle">{{ shortenText(book.book_name) }}</p>
          <p class="bookAuthor">
            AUTHOR: <span>{{ book.author_name }}</span>
          </p>
          <p class="bookAuthor">
            GENRE: <span>{{ book.genre }}</span>
          </p>
        </div>
        <div class="actions">
          <div
            class="actionBtns"
            @click="confirmDelete(book.book_id, book.book_name)"
          >
            <img
              src="@/assets/images/delete-icon.png"
              alt=""
              class="actionBtnImg"
            />
            Delete
          </div>
          <div
            class="actionBtns sideBtn"
            @click="changePreviewBook(book.book_id)"
          >
            <img
              src="@/assets/images/edit-icon.png"
              alt=""
              class="actionBtnImg"
            />
            Edit
          </div>
        </div>
      </div>
      <div
        class="headBookTitleContainer"
        v-if="searchBooks.sections.length > 0"
      >
        <div class="headBookTitle">Search by Sections</div>
      </div>
      <div
        v-for="(book, index) in searchBooks.sections"
        :key="index"
        class="card myCard"
      >
        <div class="bookImgContainer">
          <img :src="book.img" alt="" class="bookImg" />
        </div>
        <div class="bookContent">
          <p class="bookTitle">{{ shortenText(book.book_name) }}</p>
          <p class="bookAuthor">
            AUTHOR: <span>{{ book.author_name }}</span>
          </p>
          <p class="bookAuthor">
            GENRE: <span>{{ book.genre }}</span>
          </p>
        </div>
        <div class="actions">
          <div
            class="actionBtns"
            @click="confirmDelete(book.book_id, book.book_name)"
          >
            <img
              src="@/assets/images/delete-icon.png"
              alt=""
              class="actionBtnImg"
            />
            Delete
          </div>
          <div
            class="actionBtns sideBtn"
            @click="changePreviewBook(book.book_id)"
          >
            <img
              src="@/assets/images/edit-icon.png"
              alt=""
              class="actionBtnImg"
            />
            Edit
          </div>
        </div>
      </div>
      <div class="headBookTitleContainer" v-if="searchBooks.genres.length > 0">
        <div class="headBookTitle">Search by Genres</div>
      </div>
      <div
        v-for="(book, index) in searchBooks.genres"
        :key="index"
        class="card myCard"
      >
        <div class="bookImgContainer">
          <img :src="book.img" alt="" class="bookImg" />
        </div>
        <div class="bookContent">
          <p class="bookTitle">{{ shortenText(book.book_name) }}</p>
          <p class="bookAuthor">
            AUTHOR: <span>{{ book.author_name }}</span>
          </p>
          <p class="bookAuthor">
            GENRE: <span>{{ book.genre }}</span>
          </p>
        </div>
        <div class="actions">
          <div
            class="actionBtns"
            @click="confirmDelete(book.book_id, book.book_name)"
          >
            <img
              src="@/assets/images/delete-icon.png"
              alt=""
              class="actionBtnImg"
            />
            Delete
          </div>
          <div
            class="actionBtns sideBtn"
            @click="changePreviewBook(book.book_id)"
          >
            <img
              src="@/assets/images/edit-icon.png"
              alt=""
              class="actionBtnImg"
            />
            Edit
          </div>
        </div>
      </div>
    </div>
    <div class="previewPanel" v-if="changeView == 2 && !addBookPallet">
      <div class="previewDetailsContainer">
        <div class="previewImgContainer">
          <img :src="previewBook.book.img" alt="" class="imgContainer" />
        </div>
        <div class="titleDiv" v-if="!isTitleEdit">
          <p class="previewTitle">
            {{ previewBook.book.book_name }}
          </p>
          <img
            src="@/assets/images/edit-icon.png"
            alt=""
            class="editActions"
            @click="editTitle()"
          />
        </div>

        <div class="previewTitleEdit" v-else>
          <input
            v-model="titleNew"
            @keyup.enter="isTitleEdit = false"
            @blur="handleTitleBlur"
            ref="titleInput"
          />
          <img
            src="@/assets/images/tick-icon.png"
            alt="Edit Title"
            title="Edit Title"
            class="editActions"
            @mousedown.prevent="saveTitle"
          />
        </div>

        <div class="majorDetails">
          <p v-if="!isAuthorEdit">
            AUTHOR: <span>{{ previewBook.book.author_name }}</span>
            <img
              src="@/assets/images/edit-icon.png"
              alt="Edit Author"
              title="Edit Author"
              class="editActions"
              @click="editAuthor()"
            />
          </p>
          <div class="editable" v-else>
            AUTHOR:
            <input
              v-model="authorNew"
              @keyup.enter="isAuthorEdit = false"
              @blur="handleAuthorBlur"
              ref="authorInput"
            />
            <img
              src="@/assets/images/tick-icon.png"
              alt="Edit Author"
              title="Edit Author"
              class="editActions"
              @mousedown.prevent="saveAuthor"
            />
          </div>
          <p v-if="!isGenreEdit">
            GENRE: <span>{{ previewBook.book.genre }}</span>
            <img
              src="@/assets/images/edit-icon.png"
              alt="Edit Genre"
              title="Edit Genre"
              class="editActions"
              @click="editGenre()"
            />
          </p>
          <div class="editable" v-else>
            GENRE:
            <input
              v-model="genreNew"
              @keyup.enter="isGenreEdit = false"
              @blur="handleGenreBlur"
              ref="genreInput"
            />
            <img
              src="@/assets/images/tick-icon.png"
              alt="Edit Genre"
              title="Edit Genre"
              class="editActions"
              @mousedown.prevent="saveGenre"
            />
          </div>

          <p>DESCRIPTION:</p>
          <p>
            <span style="margin-left: 0rem"
              >Lorem ipsum dolor sit amet consectetur adipisicing elit.
              Cupiditate repellendus quae similique natus in blanditiis
              doloribus facer?</span
            >
          </p>
        </div>
        <div class="bookStats">
          <div class="bookStatOption">
            <div class="bookStatData">{{ previewBook.issues }}</div>
            <p class="bookStatTitle"># Issues</p>
          </div>
          <div class="bookStatOption">
            <div class="bookStatData">{{ previewBook.requests }}</div>
            <p class="bookStatTitle"># Requests</p>
          </div>
          <div class="bookStatOption">
            <div class="bookStatData">{{ previewBook.avg_rating }}</div>
            <p class="bookStatTitle">Avg. Rating</p>
          </div>
        </div>
      </div>
    </div>
    <div class="mainPanel directionColumn" v-if="changeView == 3">
      <div class="headBookTitleContainer">
        <div class="headBookTitle">Issue Requests</div>
      </div>
      <div class="logHead">
        <div class="issueRow snoRow">Request Date</div>
        <div class="issueRow titleRow">Book Title</div>
        <div class="issueRow userNameRow">User Name</div>
        <div class="issueRow actionRow">Actions</div>
      </div>
      <div
        class="logHead whiteBg"
        v-for="(request, index) in allRequests"
        :key="index"
      >
        <div class="issueRow snoRow">{{ request.request_date }}</div>
        <div class="issueRow titleRow">{{ request.book_name }}</div>
        <div class="issueRow userNameRow">{{ request.user_name }}</div>
        <div class="issueRow actionRow">
          <div
            class="issueAction"
            @click="acceptIssue(request.book_id, request.user_id)"
          >
            <img
              src="@/assets/images/tick-icon.png"
              alt=""
              class="actionBtnImg"
            />
            Issue
          </div>
          <div
            class="issueAction"
            @click="rejectIssue(request.book_id, request.user_id)"
          >
            <img
              src="@/assets/images/cross-icon.png"
              alt=""
              class="actionBtnImg"
            />
            Reject
          </div>
        </div>
      </div>
    </div>
    <div class="mainPanel directionColumn" v-if="changeView == 4">
      <div class="headBookTitleContainer">
        <div class="headBookTitle">Issue Logs</div>
      </div>
      <div class="logHead">
        <div class="issueRow snoRow">Issue Date</div>
        <div class="issueRow titleRow">Book Title</div>
        <div class="issueRow userNameRow">User Name</div>
        <div class="issueRow actionRow">Return Date</div>
      </div>
      <div
        class="logHead whiteBg"
        v-for="(issue, index) in allIssues"
        :key="index"
      >
        <div class="issueRow snoRow">{{ issue.doi }}</div>
        <div class="issueRow titleRow">{{ issue.book_name }}</div>
        <div class="issueRow userNameRow">{{ issue.user_name }}</div>
        <div class="issueRow actionRow" v-if="issue.current_issue">
          <div
            class="issueAction"
            @click="revokeIssue(issue.book_id, issue.user_id)"
          >
            <img
              src="@/assets/images/return_icon.png"
              alt=""
              class="actionBtnImg"
            />
            Revoke Issue
          </div>
        </div>
        <div class="issueRow actionRow" v-else>{{ issue.dor }}</div>
      </div>
    </div>
    <div class="mainPanel withPreview" v-if="changeView == 5">
      <div class="headBookTitleContainer">
        <div class="headBookTitle">Book Management</div>
        <div class="addNewBook" @click="createBook()">Add Book</div>
      </div>
      <div v-for="(book, index) in books" :key="index" class="card myCard">
        <div class="bookImgContainer">
          <img :src="book.img" alt="" class="bookImg" />
        </div>
        <div class="bookContent">
          <p class="bookTitle">{{ shortenText(book.book_name) }}</p>
          <p class="bookAuthor">
            AUTHOR: <span>{{ book.author_name }}</span>
          </p>
          <p class="bookAuthor">
            GENRE: <span>{{ book.genre }}</span>
          </p>
        </div>
        <div class="actions">
          <div
            class="actionBtns"
            @click="confirmDelete(book.book_id, book.book_name)"
          >
            <img
              src="@/assets/images/delete-icon.png"
              alt=""
              class="actionBtnImg"
            />
            Delete
          </div>
          <div
            class="actionBtns sideBtn"
            @click="changePreviewBook(book.book_id)"
          >
            <img
              src="@/assets/images/edit-icon.png"
              alt=""
              class="actionBtnImg"
            />
            Edit
          </div>
        </div>
      </div>
    </div>
    <div class="previewPanel" v-if="changeView == 5 && !addBookPallet">
      <div class="previewDetailsContainer">
        <div class="previewImgContainer">
          <img :src="previewBook.book.img" alt="" class="imgContainer" />
        </div>
        <div class="titleDiv" v-if="!isTitleEdit">
          <p class="previewTitle">
            {{ previewBook.book.book_name }}
          </p>
          <img
            src="@/assets/images/edit-icon.png"
            alt=""
            class="editActions"
            @click="editTitle()"
          />
        </div>

        <div class="previewTitleEdit" v-else>
          <input
            v-model="titleNew"
            @keyup.enter="isTitleEdit = false"
            @blur="handleTitleBlur"
            ref="titleInput"
          />
          <img
            src="@/assets/images/tick-icon.png"
            alt="Edit Title"
            title="Edit Title"
            class="editActions"
            @mousedown.prevent="saveTitle"
          />
        </div>

        <div class="majorDetails">
          <p v-if="!isAuthorEdit">
            AUTHOR: <span>{{ previewBook.book.author_name }}</span>
            <img
              src="@/assets/images/edit-icon.png"
              alt="Edit Author"
              title="Edit Author"
              class="editActions"
              @click="editAuthor()"
            />
          </p>
          <div class="editable" v-else>
            AUTHOR:
            <input
              v-model="authorNew"
              @keyup.enter="isAuthorEdit = false"
              @blur="handleAuthorBlur"
              ref="authorInput"
            />
            <img
              src="@/assets/images/tick-icon.png"
              alt="Edit Author"
              title="Edit Author"
              class="editActions"
              @mousedown.prevent="saveAuthor"
            />
          </div>
          <p v-if="!isGenreEdit">
            GENRE: <span>{{ previewBook.book.genre }}</span>
            <img
              src="@/assets/images/edit-icon.png"
              alt="Edit Genre"
              title="Edit Genre"
              class="editActions"
              @click="editGenre()"
            />
          </p>
          <div class="editable" v-else>
            GENRE:
            <input
              v-model="genreNew"
              @keyup.enter="isGenreEdit = false"
              @blur="handleGenreBlur"
              ref="genreInput"
            />
            <img
              src="@/assets/images/tick-icon.png"
              alt="Edit Genre"
              title="Edit Genre"
              class="editActions"
              @mousedown.prevent="saveGenre"
            />
          </div>

          <p>DESCRIPTION:</p>
          <p>
            <span style="margin-left: 0rem"
              >Lorem ipsum dolor sit amet consectetur adipisicing elit.
              Cupiditate repellendus quae similique natus in blanditiis
              doloribus facer?</span
            >
          </p>
        </div>
        <div class="bookStats">
          <div class="bookStatOption">
            <div class="bookStatData">{{ previewBook.issues }}</div>
            <p class="bookStatTitle"># Issues</p>
          </div>
          <div class="bookStatOption">
            <div class="bookStatData">{{ previewBook.requests }}</div>
            <p class="bookStatTitle"># Requests</p>
          </div>
          <div class="bookStatOption">
            <div class="bookStatData">{{ previewBook.avg_rating }}</div>
            <p class="bookStatTitle">Avg. Rating</p>
          </div>
        </div>
      </div>
    </div>
    <div class="previewPanel" v-if="changeView == 5 && addBookPallet">
      <p class="previewTitle">Add New Book</p>
      <div class="previewDetailsContainer">
        <div class="createNewEntry">
          BOOK COVER URL:
          <input v-model="createBookImg" class="createNewEntryInput" />
        </div>
        <div class="createNewEntry">
          TITLE:
          <input v-model="createBookName" class="createNewEntryInput" />
        </div>
        <div class="createNewEntry">
          AUTHOR NAME:
          <input v-model="createBookAuthor" class="createNewEntryInput" />
        </div>
        <div class="createNewEntry">
          SECTION NAME:
          <select
            name="cars"
            class="createNewEntryDropDown"
            v-model="selectedSection"
            @change="getGenres()"
          >
            <option
              v-for="(dropOption, dropIndex) in sections"
              :key="dropIndex"
              :value="dropOption.section_id"
            >
              {{ dropOption.section_name }}
            </option>
          </select>
        </div>
        <div class="createNewEntry">
          GENRE:
          <select
            name="cars"
            v-model="selectedGenre"
            class="createNewEntryDropDown"
          >
            <option
              v-for="(dropOption, dropIndex) in dropGenre"
              :key="dropIndex"
              :value="dropOption"
            >
              {{ dropOption }}
            </option>
          </select>
        </div>
        <div class="submitNew" @click="submitNewBook()">SUBMIT</div>
      </div>
    </div>
    <div class="mainPanel withPreview" v-if="changeView == 6">
      <div class="headBookTitleContainer">
        <div class="headBookTitle">Section Management</div>
        <div class="addNewBook" @click="createSection()">Add Section</div>
      </div>
      <div
        v-for="(section, index) in sections"
        :key="index"
        class="authorCard"
        @click="changePreviewSection(section.section_id)"
      >
        <div class="authorImgContainer">
          <img :src="section.img" alt="" class="authorImg" />
        </div>
        <div class="authorContent">
          <p class="authorName">{{ section.section_name }}</p>
        </div>
      </div>
    </div>
    <div class="previewPanel" v-if="changeView == 6 && !addSectionPallet">
      <div class="previewDetailsContainer">
        <div class="previewImgContainer previewSectionImgContainer">
          <img
            :src="previewSection.img"
            alt=""
            class="imgContainer previewSectionImg"
          />
          <div class="downloadPDFContainer">
            <div
              class="downloadPDF"
              @click="deleteSection(previewSection.section_id)"
            >
              <img
                src="@/assets/images/delete-icon.png"
                alt="delete"
                class="pdfIcon"
              />
            </div>
          </div>
        </div>
        <div class="titleDiv" v-if="!isSectionTitleEdit">
          <p class="previewTitle">
            {{ previewSection.section_name }}
          </p>
          <img
            src="@/assets/images/edit-icon.png"
            alt=""
            class="editActions"
            @click="editSectionTitle()"
          />
        </div>
        <div class="previewTitleEdit" v-else>
          <input
            v-model="sectionTitleNew"
            @keyup.enter="isSectionTitleEdit = false"
            @blur="handleSectionTitleBlur"
            ref="sectionTitleInput"
          />
          <img
            src="@/assets/images/tick-icon.png"
            alt="Edit Section Title"
            title="Edit Section Title"
            class="editActions"
            @mousedown.prevent="saveSectionTitle"
          />
        </div>
      </div>
    </div>
    <div class="previewPanel" v-if="changeView == 6 && addSectionPallet">
      <p class="previewTitle">Add New Section</p>
      <div class="previewDetailsContainer">
        <div class="createNewEntry">
          SECTION COVER URL:
          <input v-model="createSectionImg" class="createNewEntryInput" />
        </div>
        <div class="createNewEntry">
          SECTION NAME:
          <input v-model="createSectionName" class="createNewEntryInput" />
        </div>

        <div class="submitNew" @click="submitNewSection()">SUBMIT</div>
      </div>
    </div>
    <div class="mainPanel withPreview" v-if="changeView == 7">
      <div class="headBookTitleContainer">
        <div class="headBookTitle">Author Management</div>
        <div class="addNewBook" @click="createAuthor()">Add Author</div>
      </div>
      <div
        v-for="(author, index) in authors"
        :key="index"
        class="authorCard"
        @click="changePreviewAuthor(author.author_id)"
      >
        <div class="authorImgContainer">
          <img :src="author.img" alt="" class="authorImg" />
        </div>
        <div class="authorContent">
          <p class="authorName">{{ author.author_name }}</p>
        </div>
      </div>
    </div>
    <div class="previewPanel" v-if="changeView == 7 && !addAuthorPallet">
      <div class="previewDetailsContainer">
        <div class="previewImgContainer previewSectionImgContainer">
          <img
            :src="previewAuthor.img"
            alt=""
            class="imgContainer previewSectionImg"
          />
          <div class="downloadPDFContainer">
            <div
              class="downloadPDF"
              @click="deleteAuthor(previewAuthor.author_id)"
            >
              <img
                src="@/assets/images/delete-icon.png"
                alt="delete"
                class="pdfIcon"
              />
            </div>
          </div>
        </div>
        <div class="titleDiv" v-if="!isAuthorNameEdit">
          <p class="previewTitle">
            {{ previewAuthor.author_name }}
          </p>
          <img
            src="@/assets/images/edit-icon.png"
            alt=""
            class="editActions"
            @click="editAuthorName()"
          />
        </div>
        <div class="previewTitleEdit" v-else>
          <input
            v-model="authorNameNew"
            @keyup.enter="isAuthorNameEdit = false"
            @blur="handleAuthorNameBlur"
            ref="authorNameInput"
          />
          <img
            src="@/assets/images/tick-icon.png"
            alt="Edit Section Title"
            title="Edit Section Title"
            class="editActions"
            @mousedown.prevent="saveAuthorName"
          />
        </div>
        <div class="majorDetails">
          <p v-if="!isAuthorDOBEdit">
            DATE OF BIRTH: <span>{{ previewAuthor.dob }}</span>
            <img
              src="@/assets/images/edit-icon.png"
              alt="Edit Author"
              title="Edit Author"
              class="editActions"
              @click="editAuthorDOB()"
            />
          </p>
          <div class="editable" v-else>
            DATE OF BIRTH:
            <input
              v-model="authorDOBNew"
              @keyup.enter="isAuthorDOBEdit = false"
              @blur="handleAuthorDOBBlur"
              ref="authorDOBInput"
            />
            <img
              src="@/assets/images/tick-icon.png"
              alt="Edit Author"
              title="Edit Author"
              class="editActions"
              @mousedown.prevent="saveAuthorDOB"
            />
          </div>
          <p v-if="!isAuthorDODEdit">
            DATE OF DEATH: <span>{{ previewAuthor.dod }}</span>
            <img
              src="@/assets/images/edit-icon.png"
              alt="Edit Genre"
              title="Edit Genre"
              class="editActions"
              @click="editAuthorDOD()"
            />
          </p>
          <div class="editable" v-else>
            DATE OF DEATH:
            <input
              v-model="authorDODNew"
              @keyup.enter="isAuthorDODEdit = false"
              @blur="handleAuthorDODBlur"
              ref="authorDOBInput"
            />
            <img
              src="@/assets/images/tick-icon.png"
              alt="Edit Genre"
              title="Edit Genre"
              class="editActions"
              @mousedown.prevent="saveAuthorDOD"
            />
          </div>
          <p v-if="!isAuthorCountryEdit">
            COUNTRY: <span>{{ previewAuthor.country }}</span>
            <img
              src="@/assets/images/edit-icon.png"
              alt="Edit Genre"
              title="Edit Genre"
              class="editActions"
              @click="editAuthorCountry()"
            />
          </p>
          <div class="editable" v-else>
            COUNTRY:
            <input
              v-model="authorCountryNew"
              @keyup.enter="isAuthorCountryEdit = false"
              @blur="handleAuthorCountryBlur"
              ref="authorCountryInput"
            />
            <img
              src="@/assets/images/tick-icon.png"
              alt="Edit Genre"
              title="Edit Genre"
              class="editActions"
              @mousedown.prevent="saveAuthorCountry"
            />
          </div>
          <p v-if="!isAuthorRatingEdit">
            AVG. RATING:
            <span>{{ previewAuthor.avg_rating.toFixed(1) }}</span>
            <img
              src="@/assets/images/edit-icon.png"
              alt="Edit Genre"
              title="Edit Genre"
              class="editActions"
              @click="editAuthorRating()"
            />
          </p>
          <div class="editable" v-else>
            AVG. RATING:
            <input
              v-model="authorRatingNew"
              @keyup.enter="isAuthorRatingEdit = false"
              @blur="handleAuthorRatingBlur"
              ref="authorRatingInput"
            />
            <img
              src="@/assets/images/tick-icon.png"
              alt="Edit Genre"
              title="Edit Genre"
              class="editActions"
              @mousedown.prevent="saveAuthorRating"
            />
          </div>
        </div>
      </div>
    </div>
    <div class="previewPanel" v-if="changeView == 7 && addAuthorPallet">
      <p class="previewTitle">Add New Author</p>
      <div class="previewDetailsContainer">
        <div class="createNewEntry">
          AUTHOR IMAGE URL:
          <input v-model="createAuthorImg" class="createNewEntryInput" />
        </div>
        <div class="createNewEntry">
          AUTHOR NAME:
          <input v-model="createAuthorName" class="createNewEntryInput" />
        </div>
        <div class="createNewEntry">
          DATE OF BIRTH:
          <input v-model="createAuthorDOB" class="createNewEntryInput" />
        </div>
        <div class="createNewEntry">
          DATE OF DEATH:
          <input v-model="createAuthorDOD" class="createNewEntryInput" />
        </div>
        <div class="createNewEntry">
          COUNTRY:
          <input v-model="createAuthorCountry" class="createNewEntryInput" />
        </div>
        <div class="createNewEntry">
          AVG. RATING:
          <input v-model="createAuthorRating" class="createNewEntryInput" />
        </div>

        <div class="submitNew" @click="submitNewAuthor()">SUBMIT</div>
      </div>
    </div>
    <div class="mainPanel withPreview" v-if="changeView == 8">
      <div class="headBookTitleContainer">
        <div class="headBookTitle">User Management</div>
      </div>
      <div
        v-for="(user, index) in users"
        :key="index"
        class="authorCard"
        @click="changePreviewUser(user.user_id)"
      >
        <div class="authorImgContainer userImgContainer">
          <img
            src="@/assets/images/male profile.png"
            v-if="user.gender == 'Male'"
            alt=""
            class="authorImg userImg"
          />
          <img
            src="@/assets/images/female profile.png"
            v-else
            alt=""
            class="authorImg userImg"
          />
        </div>
        <div class="authorContent">
          <p class="authorName">{{ user.user_name }}</p>
        </div>
      </div>
    </div>
    <div class="previewPanel" v-if="changeView == 8">
      <div class="userPreviewCont">
        <div
          class="previewImgContainer previewSectionImgContainer previewUserContainer"
        >
          <img
            src="@/assets/images/male profile.png"
            v-if="previewUser.gender == 'Male'"
            alt=""
            class="imgContainer previewSectionImg previewUserImg"
          />
          <img
            src="@/assets/images/female profile.png"
            v-else
            alt=""
            class="imgContainer previewSectionImg previewUserImg"
          />
        </div>
        <div class="titleDiv">
          <p class="previewTitle">
            {{ previewUser.user_name }}
          </p>
        </div>
        <div class="majorDetails">
          <p>
            EMAIL: <span>{{ previewUser.email }}</span>
          </p>
          <p>
            DATE JOINED: <span>{{ previewUser.doj }}</span>
          </p>
          <p>
            LAST LOGED: <span>{{ previewUser.last_loged }}</span>
          </p>
        </div>
        <div class="userStatistics">
          <div class="userLeague">
            <img
              v-if="userStats.rank == 'Sage'"
              src="@/assets/images/Sage_logo.png"
              :alt="`${userStats.rank} League`"
              class="rankLogo"
            />
            <img
              v-if="userStats.rank == 'Scholar'"
              src="@/assets/images/Scholar_logo.png"
              :alt="`${userStats.rank} League`"
              class="rankLogo"
            />
            <img
              v-if="userStats.rank == 'Literati'"
              src="@/assets/images/Literati_logo.png"
              :alt="`${userStats.rank} League`"
              class="rankLogo"
            />
            <img
              v-if="userStats.rank == 'Reader'"
              src="@/assets/images/Reader_logo.png"
              :alt="`${userStats.rank} League`"
              class="rankLogo"
            />
          </div>
          <div class="userStatsData">
            <p class="league">{{ userStats.rank }} League</p>
            <div class="score">
              {{ userStats.score }}
              <img
                src="@/assets/images/points.png"
                alt="points"
                class="scorePoint"
              />
            </div>
          </div>
        </div>
        <div class="bookStats">
          <div class="bookStatOption">
            <div class="bookStatData">{{ userStats.numIssues }}</div>
            <p class="bookStatTitle"># Issues</p>
          </div>
          <div class="bookStatOption">
            <div class="bookStatData">{{ userStats.numRequests }}</div>
            <p class="bookStatTitle"># Requests</p>
          </div>
          <div class="bookStatOption">
            <div class="bookStatData">{{ userStats.avg_rating }}</div>
            <p class="bookStatTitle">Avg. Rating</p>
          </div>
        </div>
      </div>

      <div class="userActions">
        <div
          class="actionBtns userActionBtns"
          title="Permanent Ban"
          @click="banUser(previewUser.user_id)"
          v-if="banData.ban_type != 'Perma'"
        >
          <img src="@/assets/images/ban-icon.png" alt="" class="actionBtnImg" />
          Ban
        </div>
        <div
          class="actionBtns userActionBtns revokeBan"
          title="Permanent Ban"
          @click="revokeBan(previewUser.user_id)"
          v-else
        >
          <img src="@/assets/images/ban-icon.png" alt="" class="actionBtnImg" />
          Un-Ban
        </div>

        <div
          class="actionBtns userActionBtns sideBtn"
          title="Temporary Ban for 30 Days"
          @click="interdictUser(previewUser.user_id)"
          v-if="banData.ban_type != 'Temp'"
        >
          <img
            src="@/assets/images/Interdict-icon.png"
            alt=""
            class="actionBtnImg"
          />
          Interdict
        </div>
        <div
          class="actionBtns userActionBtns sideBtn"
          :title="`To be lifted on ${banData.ban_end_date}`"
          @click="revokeInterdict(previewUser.user_id)"
          v-else
        >
          <img
            src="@/assets/images/Interdict-icon.png"
            alt=""
            class="actionBtnImg"
          />
          De-Interdict
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "@/axios";
import SideNav from "@/components/SideNav.vue";
import BarChartView from "@/components/BarChartView.vue";
import PieChartView from "@/components/PieChartView.vue";
import DataCards from "@/components/DataCards.vue";
import LibrarianBooksStats from "@/components/LibrarianBooksStats.vue";
import LibrarianAuthorsStats from "@/components/LibrarianAuthorsStats.vue";
export default {
  components: {
    SideNav,
    BarChartView,
    PieChartView,
    DataCards,
    LibrarianBooksStats,
    LibrarianAuthorsStats,
  },
  name: "LibrarianView",
  data() {
    return {
      statsTab: 1,
      userStatsData: {},
      bookStatsData: {},
      authorsStatsData: {},
      searchBooks: {
        titles: [],
        authors: [],
        sections: [],
        genres: [],
      },
      books: [],
      sections: [],
      authors: [],
      users: [],
      genres: [],
      dropGenre: [],
      previewBook: {},
      previewSection: {},
      previewAuthor: {},
      previewUser: {},
      userStats: {},
      allRequests: [],
      allIssues: [],
      banData: {},
      changeView: 1,
      isTitleEdit: false,
      isAuthorEdit: false,
      isGenreEdit: false,
      isSectionTitleEdit: false,
      isAuthorNameEdit: false,
      isAuthorDOBEdit: false,
      isAuthorDODEdit: false,
      isAuthorCountryEdit: false,
      isAuthorRatingEdit: false,
      titleNew: "",
      genreNew: "",
      authorNew: "",
      sectionTitleNew: "",
      authorNameNew: "",
      authorDOBNew: "",
      authorDODNew: "",
      authorCountryNew: "",
      authorRatingNew: "",
      addBookPallet: false,
      addSectionPallet: false,
      addAuthorPallet: false,
      createBookImg: "",
      createBookName: "",
      createBookAuthor: "",
      selectedSection: "",
      selectedGenre: "",
      createSectionName: "",
      createSectionImg: "",
      createAuthorImg: "",
      createAuthorName: "",
      createAuthorDOB: "",
      createAuthorDOD: "",
      createAuthorCountry: "",
      createAuthorRating: "",
      selectedBookId: null,
    };
  },
  created() {
    this.changeView = 1;
    this.statsTab = 1;
    this.fetchUsersStats();
    this.fetchBooksStats();
    this.fetchAuthorsStats();
  },
  watch: {
    keyword(newKeyword) {
      this.bookSearcher(newKeyword);
    },
    selectedBookId(newBookId) {
      this.changePreviewBook(newBookId);
    },
  },
  methods: {
    changeMiddleView(view) {
      this.changeView = view;
      if (view == 1) {
        this.fetchUsersStats();
      } else if (view == 2) {
        this.fetchLatest();
      } else if (view == 3) {
        this.fetchRequests();
      } else if (view == 4) {
        this.fetchIssues();
      } else if (view == 5) {
        this.fetchBooks();
      } else if (view == 6) {
        this.fetchSections();
      } else if (view == 7) {
        this.fetchAuthors();
      } else if (view == 8) {
        this.fetchUsers();
      }
    },
    fetchLatest() {
      axios
        .get(`http://192.168.1.3:5000/get-content/librarian/latestBooks`)
        .then((response) => {
          this.searchBooks = {
            titles: [],
            authors: [],
            sections: [],
            genres: [],
          };
          this.changePreviewBook(response.data[0].book_id);
        })
        .catch(() => {
          this.$router.push("/error");
        });
    },
    bookSearcher() {
      let keyword = document.getElementById("searchbox").value;
      axios
        .get(`http://192.168.1.3:5000/search-content?keyword=${keyword}`, {
          params: {
            keyword: keyword,
          },
        })
        .then((response) => {
          this.searchBooks = {
            titles: [],
            authors: [],
            sections: [],
            genres: [],
          };
          this.searchBooks.titles = response.data.titles;
          this.searchBooks.authors = response.data.authors;
          this.searchBooks.genres = response.data.genres;
          this.searchBooks.sections = response.data.sections;
          console.log(this.searchBooks);
          if (this.searchBooks.titles.length != 0) {
            this.changePreviewBook(this.searchBooks.titles[0].book_id);
          } else if (this.searchBooks.authors.length != 0) {
            this.changePreviewBook(this.searchBooks.authors[0].book_id);
          } else if (this.searchBooks.sections.length != 0) {
            this.changePreviewBook(this.searchBooks.sections[0].book_id);
          } else if (this.searchBooks.genres.length != 0) {
            this.changePreviewBook(this.searchBooks.genres[0].book_id);
          }
        })
        .catch(() => {});
    },
    changeStatsTab(tab) {
      this.statsTab = tab;
      const elements = document.querySelectorAll("dashTab");
      elements.forEach((ele) => {
        ele.classList.remove("currentDashtab");
      });
      this.$refs[`tab${tab}`].classList.add("currentDashtab");
      if (tab == 1) {
        this.fetchUsersStats();
      } else if (tab == 2) {
        this.fetchBooksStats();
      } else if (tab == 3) {
        this.fetchAuthorsStats();
      }
    },
    fetchAuthorsStats() {
      axios
        .get(`http://192.168.1.3:5000/get-statistics/librarian/authors`)
        .then((response) => {
          this.authorsStatsData = response.data;
          console.log(this.bookStatsData);
        })
        .catch(() => {
          this.$router.push("/error");
        });
    },
    fetchBooksStats() {
      axios
        .get(`http://192.168.1.3:5000/get-statistics/librarian/books`)
        .then((response) => {
          this.bookStatsData = response.data;
          console.log(this.bookStatsData);
        })
        .catch(() => {
          this.$router.push("/error");
        });
    },
    fetchUsersStats() {
      axios
        .get(`http://192.168.1.3:5000/get-statistics/librarian/users`)
        .then((response) => {
          this.userStatsData = response.data;
        })
        .catch(() => {
          this.$router.push("/error");
        });
    },
    async banUser(user_id) {
      try {
        const response = await axios.post(
          "http://192.168.1.3:5000/push-content/blacklists",
          {
            user_id: user_id,
            ban_type: "Perma",
          }
        );
        console.log("Success:", response.data);
        this.changePreviewUser(user_id);
        console.log("Success:", response.data);
      } catch (error) {
        alert("Unable to Ban the User.");
      }
    },
    async revokeBan(user_id) {
      try {
        const response = await axios.delete(
          `http://192.168.1.3:5000/delete-content/blacklists?user_id=${user_id}`
        );
        this.changePreviewUser(user_id);
        console.log("Success:", response.data);
      } catch (error) {
        alert("Unable to Revoke Ban the User.");
      }
    },
    async interdictUser(user_id) {
      try {
        const response = await axios.post(
          "http://192.168.1.3:5000/push-content/blacklists",
          {
            user_id: user_id,
            ban_type: "Temp",
          }
        );
        this.changePreviewUser(user_id);
        console.log("Success:", response.data);
      } catch (error) {
        alert("Unable to Ban the User.");
      }
    },
    async revokeInterdict(user_id) {
      try {
        const response = await axios.delete(
          `http://192.168.1.3:5000/delete-content/blacklists?user_id=${user_id}`
        );
        this.changePreviewUser(user_id);
        console.log("Success:", response.data);
      } catch (error) {
        alert("Unable to Revoke Interdict the User.");
      }
    },
    rejectIssue(book_id, user_id) {
      axios
        .get(
          `http://192.168.1.3:5000/delete-content/requests?book_id=${book_id}&user_id=${user_id}`
        )
        .then((response) => {
          this.fetchRequests();
          console.log(response.data);
        })
        .catch(() => {
          this.$router.push("/error");
        });
    },
    async acceptIssue(book_id, user_id) {
      try {
        const responser = await axios.get(
          `http://192.168.1.3:5000/get-librarian/current-user-issues?user_id=${user_id}`
        );
        if (responser.data.count + 1 <= 5) {
          try {
            const response = await axios.post(
              "http://192.168.1.3:5000/push-content/issues",
              {
                book_id: book_id,
                user_id: user_id,
              }
            );
            this.rejectIssue(book_id, user_id);
            console.log("Success:", response.data);
          } catch (error) {
            alert("Unable to Accept the Issue Request.");
          }
        } else {
          alert(
            "User already above Issue limit. Either Reject this request or Revoke Issue for some of the Already Issued."
          );
        }
      } catch (error) {
        this.$router.push("/error");
      }
    },

    async revokeIssue(book_id, user_id) {
      try {
        const response = await axios.put(
          "http://192.168.1.3:5000/put-content/issues",
          {
            book_id: book_id,
            user_id: user_id,
          }
        );
        console.log("Success:", response.data);
        this.fetchIssues();
      } catch (error) {
        alert(
          "Unable to submit the feedback. Kindly try again or contact the librarian."
        );
      }
    },
    fetchBooks() {
      axios
        .get("http://192.168.1.3:5000/get-content/latestBooks")
        .then((response) => {
          this.books = response.data;
          this.changePreviewBook(this.books[0].book_id);
        })
        .catch(() => {
          this.$router.push("/error");
        });
    },
    fetchSections() {
      axios
        .get("http://192.168.1.3:5000/get-content/sections")
        .then((response) => {
          this.sections = response.data;
          this.changePreviewSection(this.sections[0].section_id);
        })
        .catch(() => {
          this.$router.push("/error");
        });
    },
    fetchAuthors() {
      axios
        .get("http://192.168.1.3:5000/get-content/authors")
        .then((response) => {
          this.authors = response.data;
          this.changePreviewAuthor(this.authors[0].author_id);
        })
        .catch(() => {
          this.$router.push("/error");
        });
    },
    fetchUsers() {
      axios
        .get("http://192.168.1.3:5000/get-content/users")
        .then((response) => {
          this.users = response.data;
          this.changePreviewUser(this.users[0].user_id);
        })
        .catch(() => {
          this.$router.push("/error");
        });
    },
    fetchRequests() {
      axios
        .get("http://192.168.1.3:5000/get-librarian/requests")
        .then((response) => {
          this.allRequests = response.data;
        })
        .catch(() => {
          this.$router.push("/error");
        });
    },
    fetchIssues() {
      axios
        .get("http://192.168.1.3:5000/get-librarian/issues")
        .then((response) => {
          this.allIssues = response.data;
        })
        .catch(() => {
          this.$router.push("/error");
        });
    },
    createBook() {
      this.addBookPallet = true;
      axios
        .get("http://192.168.1.3:5000/get-content/sections")
        .then((response) => {
          this.sections = response.data;
        })
        .catch(() => {
          this.$router.push("/error");
        });
    },
    createSection() {
      this.addSectionPallet = true;
    },
    createAuthor() {
      this.addAuthorPallet = true;
    },
    getGenres() {
      axios
        .get(
          `http://192.168.1.3:5000/get-content/books?section_id=${this.selectedSection}`
        )
        .then((response) => {
          let genres = response.data.map((element) => element.genre);
          this.dropGenre = [...new Set(genres)];
        })
        .catch(() => {
          this.$router.push("/error");
        });
    },
    async submitNewBook() {
      if (
        this.createBookImg != "" &&
        this.createBookName != "" &&
        this.createBookAuthor != "" &&
        this.selectedSection != "" &&
        this.selectedGenre != ""
      ) {
        try {
          const response = await axios.post(
            "http://192.168.1.3:5000/push-content/newBook",
            {
              book_name: this.createBookName,
              img: this.createBookImg,
              author_name: this.createBookAuthor,
              section_id: this.selectedSection,
              genre: this.selectedGenre,
            }
          );
          console.log("Success:", response.data);
          this.fetchBooks();
        } catch (error) {
          if (
            error.response &&
            error.response.data &&
            error.response.data.error
          ) {
            alert(error.response.data.error);
          } else {
            alert("An unknown error occurred.");
          }
        }
      } else {
        alert("Fill all the required fields to proceed.");
      }
    },
    async submitNewSection() {
      if (this.createSectionImg != "" && this.createSectionName != "") {
        try {
          const response = await axios.post(
            "http://192.168.1.3:5000/push-content/sections",
            {
              section_name: this.createSectionName,
              img: this.createSectionImg,
            }
          );
          console.log("Success:", response.data);
          this.fetchSections();
        } catch (error) {
          console.log(error);
          if (
            error.response &&
            error.response.data &&
            error.response.data.error
          ) {
            alert(error.response.data.error);
          } else {
            alert("An unknown error occurred.");
          }
        }
      } else {
        alert("Fill all the required fields to proceed.");
      }
    },
    async submitNewAuthor() {
      if (
        this.createAuthorImg != "" &&
        this.createAuthorName != "" &&
        this.createAuthorDOB != "" &&
        this.createAuthorDOD != "" &&
        this.createAuthorCountry != "" &&
        this.createAuthorRating != ""
      ) {
        try {
          const response = await axios.post(
            "http://192.168.1.3:5000/push-content/authors",
            {
              author_name: this.createAuthorName,
              img: this.createAuthorImg,
              dob: this.createAuthorDOB,
              dod: this.createAuthorDOD,
              country: this.createAuthorCountry,
              avg_rating: this.createAuthorRating,
            }
          );
          console.log("Success:", response.data);
          this.fetchAuthors();
        } catch (error) {
          console.log(error);
          if (
            error.response &&
            error.response.data &&
            error.response.data.error
          ) {
            alert(error.response.data.error);
          } else {
            alert("An unknown error occurred.");
          }
        }
      } else {
        alert("Fill all the required fields to proceed.");
      }
    },
    editTitle() {
      this.titleNew = this.previewBook.book.book_name;
      this.isTitleEdit = true;
    },
    handleTitleBlur(event) {
      if (this.$refs.titleInput.contains(event.relatedTarget)) {
        return;
      }
      this.isTitleEdit = false;
    },
    async saveTitle(event) {
      event.stopPropagation();
      try {
        const response = await axios.put(
          "http://192.168.1.3:5000/put-content/books",
          {
            book_id: this.previewBook.book.book_id,
            book_name: this.titleNew,
          }
        );
        this.previewBook.book.book_name = this.titleNew;
        this.isTitleEdit = false;
        console.log("Success:", response.data);
      } catch (error) {
        alert("Unable to edit the Title. Kindly try again.");
      }
    },
    editGenre() {
      this.genreNew = this.previewBook.book.genre;
      this.isGenreEdit = true;
    },
    handleGenreBlur(event) {
      if (this.$refs.genreInput.contains(event.relatedTarget)) {
        return;
      }
      this.isGenreEdit = false;
    },
    async saveGenre(event) {
      event.stopPropagation();
      try {
        const response = await axios.put(
          "http://192.168.1.3:5000/put-content/books",
          {
            book_id: this.previewBook.book.book_id,
            genre: this.genreNew,
          }
        );
        this.previewBook.book.genre = this.genreNew;
        this.isGenreEdit = false;
        console.log("Success:", response.data);
      } catch (error) {
        alert("Unable to edit the Genre. Kindly try again.");
      }
    },
    editAuthor() {
      this.authorNew = this.previewBook.book.author_name;
      this.isAuthorEdit = true;
    },
    handleAuthorBlur(event) {
      if (this.$refs.authorInput.contains(event.relatedTarget)) {
        return;
      }
      this.isAuthorEdit = false;
    },
    async saveAuthor(event) {
      event.stopPropagation();
      try {
        const response = await axios.put(
          "http://192.168.1.3:5000/put-content/books",
          {
            book_id: this.previewBook.book.book_id,
            author_name: this.authorNew,
          }
        );
        const responseAuthor = await axios.put(
          "http://192.168.1.3:5000/put-content/authors",
          {
            author_id: this.previewBook.book.author_id,
            author_name: this.authorNew,
          }
        );
        this.previewBook.book.author_name = this.authorNew;
        this.isAuthorEdit = false;
        console.log("Success:", response.data, responseAuthor.data);
      } catch (error) {
        alert("Unable to edit the Author Name. Kindly try again.");
      }
    },
    editSectionTitle() {
      this.sectionTitleNew = this.previewSection.section_name;
      this.isSectionTitleEdit = true;
    },
    handleSectionTitleBlur(event) {
      if (this.$refs.sectionTitleInput.contains(event.relatedTarget)) {
        return;
      }
      this.isSectionTitleEdit = false;
    },
    async saveSectionTitle(event) {
      event.stopPropagation();
      try {
        const response = await axios.put(
          "http://192.168.1.3:5000/put-content/sections",
          {
            section_id: this.previewSection.section_id,
            section_name: this.sectionTitleNew,
          }
        );
        this.previewSection.section_name = this.sectionTitleNew;
        this.isSectionTitleEdit = false;
        console.log("Success:", response.data);
      } catch (error) {
        alert("Unable to edit the Section Name. Kindly try again.");
      }
    },
    editAuthorName() {
      this.authorNameNew = this.previewAuthor.author_name;
      this.isAuthorNameEdit = true;
    },
    handleAuthorNameBlur(event) {
      if (this.$refs.authorNameInput.contains(event.relatedTarget)) {
        return;
      }
      this.isAuthorNameEdit = false;
    },
    async saveAuthorName(event) {
      event.stopPropagation();
      try {
        const response = await axios.put(
          "http://192.168.1.3:5000/put-content/authors",
          {
            author_id: this.previewAuthor.author_id,
            author_name: this.authorNameNew,
          }
        );
        this.previewAuthor.author_name = this.authorNameNew;
        this.isAuthorNameEdit = false;
        console.log("Success:", response.data);
      } catch (error) {
        alert("Unable to edit the Author Name. Kindly try again.");
      }
    },
    editAuthorDOB() {
      this.authorDOBNew = this.previewAuthor.dob;
      this.isAuthorDOBEdit = true;
    },
    handleAuthorDOBBlur(event) {
      if (this.$refs.authorDOBInput.contains(event.relatedTarget)) {
        return;
      }
      this.isAuthorDOBEdit = false;
    },
    async saveAuthorDOB(event) {
      event.stopPropagation();
      try {
        const response = await axios.put(
          "http://192.168.1.3:5000/put-content/authors",
          {
            author_id: this.previewAuthor.author_id,
            dob: this.authorDOBNew,
          }
        );
        this.previewAuthor.dob = this.authorDOBNew;
        this.isAuthorDOBEdit = false;
        console.log("Success:", response.data);
      } catch (error) {
        alert("Unable to edit the Author DOB. Kindly try again.");
      }
    },
    editAuthorDOD() {
      this.authorDODNew = this.previewAuthor.dod;
      this.isAuthorDODEdit = true;
    },
    handleAuthorDODBlur(event) {
      if (this.$refs.authorDODInput.contains(event.relatedTarget)) {
        return;
      }
      this.isAuthorDODEdit = false;
    },
    async saveAuthorDOD(event) {
      event.stopPropagation();
      try {
        const response = await axios.put(
          "http://192.168.1.3:5000/put-content/authors",
          {
            author_id: this.previewAuthor.author_id,
            dod: this.authorDODNew,
          }
        );
        this.previewAuthor.dod = this.authorDODNew;
        this.isAuthorDODEdit = false;
        console.log("Success:", response.data);
      } catch (error) {
        alert("Unable to edit the Author DOD. Kindly try again.");
      }
    },
    editAuthorCountry() {
      this.authorCountryNew = this.previewAuthor.country;
      this.isAuthorCountryEdit = true;
    },
    handleAuthorCountryBlur(event) {
      if (this.$refs.authorCountryInput.contains(event.relatedTarget)) {
        return;
      }
      this.isAuthorCountryEdit = false;
    },
    async saveAuthorCountry(event) {
      event.stopPropagation();
      try {
        const response = await axios.put(
          "http://192.168.1.3:5000/put-content/authors",
          {
            author_id: this.previewAuthor.author_id,
            country: this.authorCountryNew,
          }
        );
        this.previewAuthor.country = this.authorCountryNew;
        this.isAuthorCountryEdit = false;
        console.log("Success:", response.data);
      } catch (error) {
        alert("Unable to edit the Author Country. Kindly try again.");
      }
    },
    editAuthorRating() {
      this.authorRatingNew = this.previewAuthor.avg_rating;
      this.isAuthorRatingEdit = true;
    },
    handleAuthorRatingBlur(event) {
      if (this.$refs.authorRatingInput.contains(event.relatedTarget)) {
        return;
      }
      this.isAuthorRatingEdit = false;
    },
    async saveAuthorRating(event) {
      event.stopPropagation();
      try {
        const response = await axios.put(
          "http://192.168.1.3:5000/put-content/authors",
          {
            author_id: this.previewAuthor.author_id,
            avg_rating: this.authorRatingNew,
          }
        );
        this.previewAuthor.avg_rating = this.authorRatingNew;
        this.isAuthorRatingEdit = false;
        console.log("Success:", response.data);
      } catch (error) {
        alert("Unable to edit the Author Avg Rating. Kindly try again.");
      }
    },
    async deleteBook(book_id) {
      try {
        const response = await axios.delete(
          `http://192.168.1.3:5000/delete-content/books?book_id=${book_id}`
        );
        console.log("Success:", response.data);
        this.fetchBooks();
      } catch (error) {
        alert("Unable to Delete the book. Kindly try again.");
      }
    },
    async deleteSection(section_id) {
      try {
        const response = await axios.delete(
          `http://192.168.1.3:5000/delete-content/sections?section_id=${section_id}`
        );
        console.log("Success:", response.data);
        this.fetchSections();
      } catch (error) {
        alert("Unable to Delete the section. Kindly try again.");
      }
    },
    async deleteAuthor(author_id) {
      try {
        const response = await axios.delete(
          `http://192.168.1.3:5000/delete-content/authors?author_id=${author_id}`
        );
        console.log("Success:", response.data);
        this.fetchAuthors();
      } catch (error) {
        alert("Unable to Delete the section. Kindly try again.");
      }
    },
    confirmDelete(book_id, book_name) {
      if (
        confirm(`Are you sure you want to delete this book : ${book_name}?`)
      ) {
        this.deleteBook(book_id, book_name);
      }
    },
    changePreviewBook(book_id) {
      this.addBookPallet = false;
      axios
        .get(
          `http://192.168.1.3:5000/get-librarian/previewBook?book_id=${book_id}`
        )
        .then((response) => {
          this.previewBook = response.data;
          this.previewBook.avg_rating = this.previewBook.avg_rating.toFixed(1);
        })
        .catch(() => {
          this.$router.push("/error");
        });
    },
    changePreviewSection(section_id) {
      this.addSectionPallet = false;
      console.log(section_id);
      axios
        .get(
          `http://192.168.1.3:5000/get-librarian/previewSection?section_id=${section_id}`
        )
        .then((response) => {
          this.previewSection = response.data;
          // this.previewBook.avg_rating = this.previewBook.avg_rating.toFixed(1);
        })
        .catch(() => {
          this.$router.push("/error");
        });
    },
    changePreviewAuthor(author_id) {
      this.addAuthorPallet = false;
      axios
        .get(
          `http://192.168.1.3:5000/get-content/authors?author_id=${author_id}`
        )
        .then((response) => {
          this.previewAuthor = response.data[0];
          // this.previewBook.avg_rating = this.previewBook.avg_rating.toFixed(1);
        })
        .catch(() => {
          this.$router.push("/error");
        });
    },
    changePreviewUser(user_id) {
      axios
        .get(`http://192.168.1.3:5000/get-content/users?user_id=${user_id}`)
        .then((response) => {
          this.previewUser = response.data[0];
          this.previewUser.doj = this.formatDate(this.previewUser.doj);
          this.previewUser.last_loged = this.formatDate(
            this.previewUser.last_loged
          );

          axios
            .get(
              `http://192.168.1.3:5000/get-statistics?user_id=${response.data[0].user_id}`
            )
            .then((responseStats) => {
              this.userStats = responseStats.data;
            })
            .catch(() => {
              this.userStats = {
                rank: "No",
                score: Math.floor(Math.random() * 301),
                numRequests: 0,
                numIssues: 0,
                avg_rating: 0.0,
              };
            });

          axios
            .get(
              `http://192.168.1.3:5000/get-content/blacklists?user_id=${user_id}`
            )
            .then((response) => {
              this.banData["ban_type"] = response.data[0].ban_type;
              this.banData["ban_date"] = response.data[0].ban_date;
              this.banData["ban_end_date"] = response.data[0].ban_end_date;
            })
            .catch(() => {
              this.banData["ban_type"] = "none";
            });
          console.log(this.banData);
        })
        .catch(() => {
          this.$router.push("/error");
        });
    },
    shortenText(text) {
      if (text.length > 35) {
        return `${text.substring(0, 35)}...`;
      } else {
        return text;
      }
    },
    formatDate(dateString) {
      const date = new Date(dateString);
      const day = date.getDate().toString().padStart(2, "0");
      const month = date.toLocaleString("default", { month: "short" });
      const year = date.getFullYear();
      const formattedDate = `${day} ${month} ${year}`;

      return formattedDate;
    },
  },
};
</script>

<style scoped>
.middle {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  width: 100%;
  height: 40.1rem;
  background: url("@/assets/images/biblio_bg.jpg");
  background-position: center center;
  background-size: cover;
  background-repeat: no-repeat;
}
.mainPanel {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  width: 95%;
  height: 100%;
  padding-bottom: 1.4rem;
  padding-top: 0.7rem;
  overflow: hidden;
  overflow-y: scroll;
}
.withPreview {
  width: 75%;
}
.previewPanel {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  width: 20%;
  height: 100%;
  background: url("https://thumbs.dreamstime.com/b/paper-texture-1847313.jpg");
  background-position: center center;
  background-size: cover;
  background-repeat: no-repeat;
}
.previewDetailsContainer {
  display: block;
  flex-direction: column;
  flex-wrap: wrap;
  justify-content: center;
  width: 100%;
  height: 100%;
  padding: 1rem 1.5rem;
  overflow: hidden;
  overflow-y: scroll;
}
.userPreviewCont {
  display: block;
  flex-direction: column;
  flex-wrap: wrap;
  justify-content: center;
  width: 100%;
  height: 92%;
  padding: 1rem 1.5rem;
  overflow: hidden;
  overflow-y: scroll;
}
.card {
  display: flex;
  flex-direction: column;
  height: 20rem;
  width: 15rem;
  cursor: pointer;
  margin: 0.7rem 1.4rem;
  border-radius: 0.3rem;
  box-shadow: 0 0.25rem 1rem #00000026;
  transition: all 0.2s ease;
  background-color: white;
}
.card:hover {
  height: 21rem;
  width: 16rem;
  margin: 0.2rem 0.9rem;
}
.myCard {
  height: 23rem;
  z-index: 1;
}
.myCard:hover {
  height: 24rem;
}
.bookImgContainer {
  display: flex;
  justify-content: center;
  height: 70%;
  width: 100%;
  overflow: hidden;
}
.bookTitle {
  transition: all 0.2s ease;
  line-height: 20px;
  margin-bottom: 0.5rem;
}
.bookImg {
  height: 100%;
  width: auto;
}
.userImg {
  height: 80%;
}
.bookContent {
  height: 30%;
  padding: 0.5rem 1rem;
  transition: all 0.2s ease;
}
.bookDetails {
  display: flex;
  transition: all 0.2s ease;
}
.bookAuthor {
  width: 100%;
  font-size: 0.7rem;
  font-weight: 600;
  color: rgb(61, 61, 61);
  transition: all 0.2s ease;
}
.bookAuthor span {
  font-weight: 500;
  transition: all 0.2s ease;
}
.actions {
  display: flex;
  width: 100%;
  height: 3rem;
  background-color: #25352b;
  z-index: 3;
}
.userActions {
  display: flex;
  width: 100%;
  height: 8%;
  background-color: #25352b;
}
.actionBtns {
  display: flex;
  justify-content: center;
  align-items: center;
  color: #e6ac45;
  width: 50%;
  cursor: pointer;
  font-size: 0.9rem;
  /* font-weight: 600; */
  transition: all 0.2s ease;
}
.userActionBtns {
  font-size: 1rem;
  /* font-weight: 600; */
}
.actionBtnImg {
  height: 1.3rem;
  width: auto;
  margin-right: 0.2rem;
  transition: all 0.2s ease;
}
.sideBtn {
  background-color: white;
}
.previewImgContainer {
  display: flex;
  justify-content: center;
  height: 20rem;
  width: 100%;
  position: relative;
}
.previewSectionImgContainer {
  height: 15rem;
  width: 15rem;
  border-radius: 10rem;
}
.previewUserContainer {
  align-items: center;
  background-color: white;
}
.previewUserImg {
  height: 80% !important;
}
.previewSectionImg {
  object-fit: cover;
}
.editable {
  display: flex;
}
.imgContainer {
  height: 100%;
  width: auto;
}
.previewTitle {
  display: flex;
  align-items: center;
  margin-top: 1rem;
  line-height: 20px;
  font-weight: 600;
  font-size: 1.1rem;
  padding: 0.2rem 0rem;
}
.previewTitle img {
  height: 1.2rem;
  width: auto;
  margin-left: 0.3rem;
  cursor: pointer;
  filter: grayscale(100%) brightness(0.2);
}
.majorDetails {
  height: max-content;
  width: 100%;
  margin: 1rem 0rem;
}
.majorDetails p {
  display: flex;
  align-items: center;
  font-size: 0.8rem;
  font-weight: 600;
  color: rgb(61, 61, 61);
  letter-spacing: 1px;
}
.majorDetails div {
  display: flex;
  align-items: center;
  font-size: 0.8rem;
  font-weight: 600;
  color: rgb(61, 61, 61);
  letter-spacing: 1px;
}
.majorDetails p > img {
  height: 1rem;
  width: auto;
  margin-left: 0.3rem;
  cursor: pointer;
  filter: grayscale(100%) brightness(0.2);
}
.majorDetails div > img {
  height: 1rem;
  width: auto;
  margin-left: 0.3rem;
  cursor: pointer;
  filter: grayscale(100%) brightness(0.2);
}
.majorDetails span {
  font-weight: 500;
  letter-spacing: 0rem;
  margin-left: 0.3rem;
}
.majorDetails input {
  font-weight: 500;
  margin-left: 0.3rem;
  padding: 0rem 0.2rem;
  border-radius: 0.2rem;
  outline: none;
  border: 1px solid rgb(61, 61, 61);
  font-size: 0.7rem;
  font-weight: 500;
  color: rgb(61, 61, 61);
}
.bookStats {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  margin: 1rem 0rem;
  height: max-content;
}
.previewTitleEdit {
  display: flex;
  align-items: center;
  margin-top: 1rem;
  line-height: 20px;
  font-weight: 600;
  font-size: 1.1rem;
  padding: 0.2rem 0rem;
}
.previewTitleEdit input {
  font-weight: 600;
  padding: 0rem 0.2rem;
  border-radius: 0.2rem;
  outline: none;
  border: 1px solid rgb(61, 61, 61);
  font-size: 1rem;
  color: rgb(61, 61, 61);
}
.previewTitleEdit img {
  height: 1rem;
  width: auto;
  margin-left: 0.3rem;
  cursor: pointer;
  filter: grayscale(100%) brightness(0.2);
}
.bookStatOption {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 5rem;
  width: 30%;
  margin: 0rem 0.5rem;
}
.bookStatData {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 3rem;
  width: 3rem;
  margin: 0.5rem;
  background-color: white;
  border-radius: 10rem;
  font-size: 1rem;
  font-weight: 600;
  box-shadow: 0 0.25rem 1rem #00000026;
  transition: all 0.2s ease;
  cursor: pointer;
  color: #e6ac45;
  background-color: #25352b;
}
.bookStatTitle {
  height: 1rem;
  width: 100%;
  font-size: 0.7rem;
  text-align: center;
}
.titleDiv {
  display: flex;
  align-items: center;
}
.titleDiv p {
  max-width: 90%;
  width: max-content;
}
.titleDiv img {
  height: 1rem;
  width: auto;
  margin-top: 1rem;
  margin-left: 0.3rem;
  filter: grayscale(100%) brightness(0);
}
.headBookTitleContainer {
  display: flex;
  flex-direction: row;
  align-items: center;
  width: 100%;
  height: 5rem;
  margin-left: 1.4rem;
}
.headBookTitle {
  display: flex;
  width: 80%;
  font-weight: 600;
  font-size: 1.1rem;
  letter-spacing: 0.5px;
}
.addNewBook {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 20%;
  height: 2.5rem;
  margin: 0rem 1.4rem;
  font-weight: 600;
  background-color: white;
  color: #e6ac45;
  border-radius: 0.5rem;
  box-shadow: 0 0.25rem 1rem #00000026;
  cursor: pointer;
  letter-spacing: 1px;
  transition: all 0.2s ease;
}
.addNewBook:hover {
  background-color: #25352b;
  color: #e6ac45;
}
.createNewEntry {
  display: flex;
  flex-direction: column;
  margin-bottom: 0.5rem;
  width: 100%;
  font-weight: 600;
  font-size: 0.8rem;
}
.createNewEntryInput {
  font-weight: 500;
  padding: 0.2rem 0.2rem;
  border-radius: 0.2rem;
  outline: none;
  border: 1px solid rgb(61, 61, 61);
  font-size: 0.8rem;
  font-weight: 500;
  color: rgb(61, 61, 61);
}
.submitNew {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  background-color: #25352b;
  color: #e6ac45;
  padding: 0.5rem;
  margin-top: 1rem;
  border-radius: 0.25rem;
  font-weight: 600;
  letter-spacing: 1px;
  cursor: pointer;
  transition: all 0.2s ease;
}
.submitNew:hover {
  background-color: #111914;
}
.createNewEntryDropDown {
  padding: 0.2rem 0.2rem;
  border-radius: 0.2rem;
  outline: none;
}
.authorCard {
  display: flex;
  flex-direction: column;
  align-items: center;
  height: 13rem;
  width: 10rem;
  margin: 0.7rem 1.4rem;
  cursor: pointer;
}
.authorImgContainer {
  display: flex;
  height: 10rem;
  width: 10rem;
  border-radius: 10rem;
  box-shadow: 0 0.25rem 1rem #00000026;
}
.userImgContainer {
  justify-content: center;
  align-items: center;
  background-color: white;
}
.authorImg {
  height: 100%;
  width: auto;
  object-fit: cover;
}
.userImg {
  height: 80%;
}
.authorContent {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
  height: 3rem;
}
.authorName {
  text-align: center;
  margin-top: 0.5rem;
  font-size: 0.9rem;
  font-weight: 700;
}
.downloadPDFContainer {
  position: absolute;
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: end;
  z-index: 1;
}
.downloadPDF {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 2rem;
  width: 2rem;
  padding: 0.4rem;
  border-radius: 30rem;
  margin-bottom: 0.8rem;
  background-color: white;
  position: relative;
  cursor: pointer;
  box-shadow: 0 0.25rem 1rem #00000026;
  z-index: 2;
  transition: all 0.2s ease;
}
.downloadPDF:hover {
  background-color: #25352b;
}
.downloadPDF:hover .pdfIcon {
  filter: none;
}
.pdfIcon {
  width: auto;
  height: 100%;
  filter: grayscale(100%) brightness(0);
}
.userStatistics {
  display: flex;
  height: 5rem;
  align-items: center;
}
.userLeague {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 3.5rem;
  width: 3.5rem;
  margin: 1rem;
  margin-left: 0rem;
  border-radius: 10rem;
  background-color: #25352b;
}
.userStatsData {
  display: flex;
  flex-direction: column;
  justify-content: center;
  height: 3.4rem;
}
.rankLogo {
  height: 80%;
  width: auto;
}
.league {
  font-size: 1.1rem;
  font-weight: 600;
  height: 1.8rem;
  font-style: italic;
  color: rgb(61, 61, 61);
  padding: 0rem 0.2rem;
}
.score {
  display: flex;
  flex-direction: row;
  align-items: center;
  height: 2rem;
  width: 100%;
  color: #e6ac45;
  font-weight: 600;
  font-size: 1rem;
  padding: 0rem 0.2rem;
}
.scorePoint {
  height: 80%;
  width: auto;
  margin-left: 0.3rem;
}
.directionColumn {
  flex-direction: column;
  align-items: center;
  justify-content: start;
  flex-wrap: nowrap;
}
.logHead {
  display: flex;
  flex-direction: row;
  min-height: 3rem;
  height: max-content;
  width: 95%;
}
.logHead .issueRow {
  color: rgb(96, 96, 96);
  font-weight: 600;
  letter-spacing: 1px;
}
.whiteBg {
  background: #ffffff;
  margin-bottom: 1rem;
  border-radius: 0.5rem;
  min-height: 4rem;
}
.whiteBg .issueRow {
  color: rgb(23, 23, 23);
  font-weight: 500;
  letter-spacing: 0.5px;
  box-shadow: 0 0.25rem 1rem #00000026;
  /* height: 3.6rem; */
}
.issueRow {
  display: flex;
  /* justify-content: center; */
  align-items: center;
  padding: 0.5rem 1rem;
  min-height: 100%;
  height: max-content;
  position: relative;
}
.whiteBg .issueRow::before {
  content: "";
  position: absolute;
  right: 0;
  top: 0.5rem;
  bottom: 0.5rem;
  width: 0;
  border-right: 4px solid rgb(0, 0, 0);
  border-radius: 100%;
}
.whiteBg .issueRow:last-child::before {
  content: "";
  position: absolute;
  right: 0;
  top: 0.5rem;
  bottom: 0.5rem;
  width: 0;
  border-right: 0rem;
}
.snoRow {
  width: 12%;
}
.titleRow {
  width: 43%;
}
.userNameRow {
  width: 25%;
}
.actionRow {
  width: 20%;
  justify-content: center;
}
.issueAction {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 0.5rem 1rem;
  box-shadow: 0 0.25rem 1rem #00000026;
  border-radius: 0.5rem;
  color: #e6ac45;
  cursor: pointer;
}
.issueAction:first-child {
  background: #25352b;
  margin-right: 1rem;
}
.issueAction img {
  margin-right: 0.5rem;
}
.dashRow {
  display: flex;
  flex-direction: row;
  align-items: center;
  height: max-content;
  width: 100%;
  margin: 0rem 1.5rem;
  /* margin-bottom: rem; */
}
.statistics {
  display: flex;
  flex-direction: column;
  width: 100%;
  height: max-content;
}
.userBarChart {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 60%;
  height: 25rem;
  padding: 1rem 0rem;
  position: relative;
  z-index: 3;
  /* background-color: white;
  padding: 1rem 2rem; */
  /* background-color: #e6ac45; */
}
.userBarChart::before {
  content: "Past 12 Months Activity";
  padding-right: 1rem;
  font-weight: 600;
  font-size: 1rem;
  margin-top: 1.5rem;
  color: rgb(61, 61, 61);
  display: flex;
  justify-content: center;
  align-items: start;
  top: 0;
  left: auto;
  height: 100%;
  width: 100%;
  position: absolute;
  z-index: 4;
}
.coreStatistics {
  display: flex;
  flex-direction: column;
  width: 100%;
  margin: 0rem 1.4rem;
}
.myBooksHead {
  margin: 0.5rem 2.4rem;
  color: rgb(61, 61, 61);
  font-weight: 700;
}
.userDataValues {
  display: flex;
  flex-direction: row;
  /* justify-content: center; */
  align-items: center;
  flex-wrap: wrap;
  width: 40%;
  height: 25rem;
}
.leagueStats {
  display: flex;
  flex-direction: column;
  width: 60%;
  height: 18rem;
  border-radius: 1rem;
  box-shadow: 0 0.25rem 1rem #00000026;
  backdrop-filter: blur(30px);
  -webkit-backdrop-filter: blur(30px);
  border: 1px solid rgba(255, 255, 255, 0.3);
}
.userGenders {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 40%;
  height: 20rem;
  padding: 1rem 0rem;
  padding-right: 2rem;
  margin: 0rem 1rem;
  position: relative;
  z-index: 3;
}
.userGenders::before {
  content: "Genders";
  padding-right: 1.8rem;
  font-weight: 600;
  font-size: 0.8rem;
  color: rgb(61, 61, 61);
  display: flex;
  justify-content: center;
  align-items: center;
  top: 0;
  left: auto;
  height: 100%;
  width: 100%;
  position: absolute;
  z-index: 4;
}
.leagueStatsHead {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 0.3rem 0rem;
  margin: 1rem 0rem;
  height: 3rem;
  width: 100%;
  font-size: 1.1rem;
  font-weight: 600;
}
.leagueDivCont {
  display: flex;
  flex-direction: row;
  width: 100%;
  height: 17rem;
  margin: 1rem 0rem;
}
.leagueDiv {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 20%;
  height: 16rem;
}
.leagueLogoCont {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 6rem;
  width: 6rem;
  border-radius: 10rem;
  background-color: #25352b;
  padding: 1rem;
  margin: 1rem 0rem;
}
.leagueName {
  color: rgb(96, 96, 96);
  font-size: 0.9rem;
  font-style: italic;
  padding: 0rem 0.2rem;
  font-weight: 600;
  letter-spacing: 1px;
}
.leagueStat {
  font-weight: 600;
}
.dashTabsContainer {
  display: flex;
  flex-direction: row;
  align-items: center;
  padding: 0rem 2rem;
  height: 5rem;
  width: 100%;
  margin-bottom: 1rem;
}
.dashTab {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 15rem;
  height: 70%;
  color: rgb(0, 0, 0);
  cursor: pointer;
  font-weight: 500;
  /* letter-spacing: 0.8px; */
  margin: 0rem 1rem;
  border: 3px solid white;
  border-radius: 1rem;
  border: 4px solid white;
  box-shadow: 0 0.25rem 1rem #00000026;
  backdrop-filter: blur(30px);
  -webkit-backdrop-filter: blur(30px);
  border: 1px solid rgba(255, 255, 255, 0.3);
}
.currentDashTab {
  background: linear-gradient(270deg, rgb(121, 241, 164), rgb(71, 171, 168));
  color: white;
}
.searchCont {
  display: flex;
  margin-top: 0.3rem;
  margin-bottom: 1rem;
  width: 100%;
  height: 4rem;
}
.searchbox {
  display: flex;
  align-items: center;
  width: 40%;
  background-color: #111914;
  border-top-right-radius: 10rem;
  border-bottom-right-radius: 10rem;
}
.search {
  margin: 1rem 1rem;
  margin-right: 2rem;
  caret-shape: bar;
  caret-color: #e6ac45;
  padding: 0.3rem 0.3rem;
  color: #e6ac45;
  font-weight: 700;
  letter-spacing: 1px;
  width: 100%;
  outline: none;
  border: 0rem;
  background-color: #111914;
  border-bottom: 3px solid #e6ac45;
}
</style>
